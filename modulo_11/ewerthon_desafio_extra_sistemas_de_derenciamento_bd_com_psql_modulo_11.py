import os
import re
import io
import csv
import sqlite3
from typing import Optional

from flask import Flask, request, jsonify, Response

DB_PATH = os.environ.get("DB_PATH", "clientes.db")
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def get_conn():
    """
    Cria uma nova conexão SQLite por chamada.
    Mantemos a row_factory para acessar colunas por nome.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def validar_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email.strip()))


def cliente_row_to_dict(row: Optional[sqlite3.Row]):
    if not row:
        return None
    return {"id": row["id"], "nome": row["nome"], "email": row["email"]}


def create_app():
    app = Flask(__name__)

    # -------------------
    # CORS simples (apenas para desenvolvimento local)
    # -------------------
    @app.after_request
    def add_cors_headers(resp):
        # Em produção, restrinja esse origin ao domínio do front-end
        resp.headers["Access-Control-Allow-Origin"] = os.environ.get("CORS_ALLOW_ORIGIN", "*")
        resp.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,PATCH,DELETE,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
        return resp

    # -------------------
    # Healthcheck
    # -------------------
    @app.route("/healthz", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    # -------------------
    # Endpoints
    # -------------------
    @app.route("/clientes", methods=["GET"])
    def listar_clientes():
        try:
            page = int(request.args.get("page", 1))
            per_page = int(request.args.get("per_page", 10))
            if page < 1 or per_page < 1:
                raise ValueError()
        except ValueError:
            return jsonify({"error": "page e per_page devem ser inteiros positivos"}), 400

        offset = (page - 1) * per_page
        filtro = request.args.get("q", None)

        sql = "SELECT id, nome, email FROM Clientes"
        params = ()
        if filtro:
            sql += " WHERE nome LIKE ? OR email LIKE ?"
            q = f"%{filtro}%"
            params = (q, q)
        sql += " ORDER BY id LIMIT ? OFFSET ?"
        params = params + (per_page, offset)

        with get_conn() as conn:
            rows = conn.execute(sql, params).fetchall()

            # total separado: usar a mesma cláusula WHERE se filtro estiver presente
            if filtro:
                total_sql = "SELECT COUNT(*) AS total FROM Clientes WHERE nome LIKE ? OR email LIKE ?"
                total_params = (q, q)
            else:
                total_sql = "SELECT COUNT(*) AS total FROM Clientes"
                total_params = ()

            total = conn.execute(total_sql, total_params).fetchone()["total"]

        clientes = [cliente_row_to_dict(r) for r in rows]
        return jsonify({
            "page": page,
            "per_page": per_page,
            "total": total,
            "clientes": clientes
        })

    @app.route("/clientes/<int:cliente_id>", methods=["GET"])
    def obter_cliente(cliente_id):
        with get_conn() as conn:
            row = conn.execute("SELECT id, nome, email FROM Clientes WHERE id = ?", (cliente_id,)).fetchone()
        if not row:
            return jsonify({"error": "Cliente não encontrado"}), 404
        return jsonify(cliente_row_to_dict(row))

    @app.route("/clientes", methods=["POST"])
    def criar_cliente():
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "JSON inválido ou cabeçalho Content-Type ausente"}), 400

        nome = (data.get("nome") or "").strip()
        email = (data.get("email") or "").strip().lower()

        if not nome or not email:
            return jsonify({"error": "nome e email são obrigatórios"}), 400
        if not validar_email(email):
            return jsonify({"error": "email inválido"}), 400

        try:
            with get_conn() as conn:
                cur = conn.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
                conn.commit()
                new_id = cur.lastrowid
        except sqlite3.IntegrityError:
            return jsonify({"error": "email já cadastrado"}), 409

        return jsonify({"id": new_id, "nome": nome, "email": email}), 201

    @app.route("/clientes/<int:cliente_id>", methods=["PUT", "PATCH"])
    def atualizar_cliente(cliente_id):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "JSON inválido"}), 400

        nome = data.get("nome")
        email = data.get("email")

        if nome is None and email is None:
            return jsonify({"error": "pelo menos 'nome' ou 'email' devem ser fornecidos"}), 400

        if email is not None:
            email = email.strip().lower()
            if not validar_email(email):
                return jsonify({"error": "email inválido"}), 400

        with get_conn() as conn:
            exists = conn.execute("SELECT id FROM Clientes WHERE id = ?", (cliente_id,)).fetchone()
            if not exists:
                return jsonify({"error": "Cliente não encontrado"}), 404

            fields = []
            params = []
            if nome is not None:
                fields.append("nome = ?"); params.append(nome.strip())
            if email is not None:
                fields.append("email = ?"); params.append(email)
            params.append(cliente_id)
            sql = "UPDATE Clientes SET " + ", ".join(fields) + " WHERE id = ?"

            try:
                cur = conn.execute(sql, params)
                conn.commit()
            except sqlite3.IntegrityError:
                return jsonify({"error": "email já cadastrado por outro cliente"}), 409

            row = conn.execute("SELECT id, nome, email FROM Clientes WHERE id = ?", (cliente_id,)).fetchone()

        return jsonify(cliente_row_to_dict(row))

    @app.route("/clientes/<int:cliente_id>", methods=["DELETE"])
    def deletar_cliente(cliente_id):
        with get_conn() as conn:
            cur = conn.execute("DELETE FROM Clientes WHERE id = ?", (cliente_id,))
            conn.commit()
            if cur.rowcount == 0:
                return jsonify({"error": "Cliente não encontrado"}), 404
        return jsonify({"deleted": cliente_id})

    @app.route("/clientes/export", methods=["GET"])
    def exportar_csv():
        with get_conn() as conn:
            rows = conn.execute("SELECT id, nome, email FROM Clientes ORDER BY id").fetchall()

        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["id", "nome", "email"])
        for r in rows:
            writer.writerow([r["id"], r["nome"], r["email"]])
        output.seek(0)

        return Response(output.getvalue(), mimetype="text/csv",
                        headers={"Content-Disposition": "attachment;filename=clientes_export.csv"})

    # -------------------
    # Error handlers (loga e retorna JSON padronizado)
    # -------------------
    @app.errorhandler(404)
    def not_found(err):
        return jsonify({"error": "Recurso não encontrado"}), 404

    @app.errorhandler(Exception)
    def handle_exception(e):
        # Log completo do exception para o terminal
        app.logger.exception("Unhandled exception:")
        return jsonify({"error": "Erro interno no servidor"}), 500

    return app


# --- Run (arquivo executável) ---
if __name__ == "__main__":
    # Configurável por variáveis de ambiente:
    # FLASK_DEBUG=1 para habilitar debug (não recomendado para produção)
    # HOST (default 127.0.0.1), PORT (default 5000)
    debug_env = os.environ.get("FLASK_DEBUG", "0")
    debug = debug_env in ("1", "true", "True")
    host = os.environ.get("HOST", "127.0.0.1")
    try:
        port = int(os.environ.get("PORT", "5000"))
    except ValueError:
        port = 5000

    app = create_app()
    # Em desenvolvimento pode usar debug=True; em produção rode via waitress/gunicorn apontando para create_app()
    app.run(debug=debug, host=host, port=port)

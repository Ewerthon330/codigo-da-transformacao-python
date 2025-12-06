import sqlite3

DB_PATH = "clientes.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def run(query, params=()):
    with get_conn() as conn:
        cur = conn.execute(query, params)
        return cur.fetchall()

def print_rows(rows):
    for r in rows:
        print(dict(r))
    if not rows:
        print("Nenhum resultado.")

if __name__ == "__main__":
    print("1) Nomes que começam com 'A'")
    print_rows(run("SELECT id, nome, email FROM Clientes WHERE nome LIKE 'A%';"))

    print("\n2) Busca case-insensitive por prefixo 'a'")
    print_rows(run("SELECT id, nome, email FROM Clientes WHERE LOWER(nome) LIKE LOWER(?);", ("a%",)))

    print("\n3) Clientes com email @gmail.com")
    print_rows(run("SELECT id, nome, email FROM Clientes WHERE email LIKE ?;", ("%@gmail.com",)))

    print("\n4) Quantidade total de clientes")
    rows = run("SELECT COUNT(*) AS total FROM Clientes;")
    print(dict(rows[0]))

    print("\n5) Quantos por domínio de email")
    q = """
    SELECT substr(email, instr(email, '@') + 1) AS dominio, COUNT(*) AS qtd
    FROM Clientes
    GROUP BY dominio
    ORDER BY qtd DESC;
    """
    print_rows(run(q))

    print("\n6) Top 5 por nome (alfabético)")
    print_rows(run("SELECT id, nome, email FROM Clientes ORDER BY nome ASC LIMIT 5;"))

    print("\n7) Paginação: página 2 (5 por página)")
    page = 2
    per_page = 5
    offset = (page - 1) * per_page
    print_rows(run("SELECT id, nome, email FROM Clientes ORDER BY id LIMIT ? OFFSET ?;", (per_page, offset)))

    print("\n8) Ordenar por tamanho do nome")
    print_rows(run("SELECT id, nome, email, LENGTH(nome) AS tam FROM Clientes ORDER BY tam DESC LIMIT 10;"))

    print("\n9) Clientes com email sem '@' (provavelmente inválidos)")
    print_rows(run("SELECT id, nome, email FROM Clientes WHERE instr(email, '@') = 0;"))

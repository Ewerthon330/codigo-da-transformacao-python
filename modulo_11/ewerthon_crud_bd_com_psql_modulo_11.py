#!/usr/bin/env python3
# clientes_crud.py
import sqlite3
from typing import List, Tuple, Optional

DB_PATH = "clientes.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # permite acessar colunas por nome
    return conn

def criar_tabela():
    sql = """
    CREATE TABLE IF NOT EXISTS Clientes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE
    );
    """
    with get_connection() as conn:
        conn.execute(sql)
        conn.commit()

def inserir_cliente(nome: str, email: str) -> int:
    sql = "INSERT INTO Clientes (nome, email) VALUES (?, ?)"
    try:
        with get_connection() as conn:
            cur = conn.execute(sql, (nome.strip(), email.strip().lower()))
            conn.commit()
            return cur.lastrowid
    except sqlite3.IntegrityError as e:
        # Provavelmente violação de UNIQUE no email
        raise ValueError("Erro: email já cadastrado ou dados inválidos.") from e

def buscar_todos() -> List[sqlite3.Row]:
    sql = "SELECT id, nome, email FROM Clientes ORDER BY id"
    with get_connection() as conn:
        cur = conn.execute(sql)
        return cur.fetchall()

def buscar_por_id(cliente_id: int) -> Optional[sqlite3.Row]:
    sql = "SELECT id, nome, email FROM Clientes WHERE id = ?"
    with get_connection() as conn:
        cur = conn.execute(sql, (cliente_id,))
        return cur.fetchone()

def buscar_por_email(email: str) -> Optional[sqlite3.Row]:
    sql = "SELECT id, nome, email FROM Clientes WHERE email = ?"
    with get_connection() as conn:
        cur = conn.execute(sql, (email.strip().lower(),))
        return cur.fetchone()

def filtrar_por_nome_inicio(prefixo: str) -> List[sqlite3.Row]:
    sql = "SELECT id, nome, email FROM Clientes WHERE nome LIKE ? ORDER BY nome"
    with get_connection() as conn:
        cur = conn.execute(sql, (f"{prefixo}%",))
        return cur.fetchall()

def atualizar_cliente(cliente_id: int, nome: str, email: str) -> bool:
    sql = "UPDATE Clientes SET nome = ?, email = ? WHERE id = ?"
    try:
        with get_connection() as conn:
            cur = conn.execute(sql, (nome.strip(), email.strip().lower(), cliente_id))
            conn.commit()
            return cur.rowcount > 0
    except sqlite3.IntegrityError as e:
        # Violação de UNIQUE no email ao tentar atualizar
        raise ValueError("Erro: email já cadastrado por outro cliente.") from e

def deletar_cliente(cliente_id: int) -> bool:
    sql = "DELETE FROM Clientes WHERE id = ?"
    with get_connection() as conn:
        cur = conn.execute(sql, (cliente_id,))
        conn.commit()
        return cur.rowcount > 0

# ---------------------------
# CLI simples para testar
# ---------------------------
def print_cliente(row: sqlite3.Row):
    if not row:
        print("Cliente não encontrado.")
        return
    print(f"id: {row['id']}  nome: {row['nome']}  email: {row['email']}")

def menu():
    criar_tabela()
    while True:
        print("\n--- CRUD Clientes ---")
        print("1) Inserir cliente")
        print("2) Listar todos")
        print("3) Buscar por id")
        print("4) Buscar por email")
        print("5) Filtrar por nome (começa com)")
        print("6) Atualizar cliente")
        print("7) Deletar cliente")
        print("0) Sair")
        opc = input("Escolha: ").strip()

        if opc == "1":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            try:
                new_id = inserir_cliente(nome, email)
                print(f"Cliente inserido com id {new_id}")
            except ValueError as e:
                print(e)

        elif opc == "2":
            rows = buscar_todos()
            if not rows:
                print("Nenhum cliente cadastrado.")
            else:
                for r in rows:
                    print_cliente(r)

        elif opc == "3":
            try:
                cid = int(input("ID do cliente: "))
                print_cliente(buscar_por_id(cid))
            except ValueError:
                print("ID inválido.")

        elif opc == "4":
            email = input("Email: ").strip()
            print_cliente(buscar_por_email(email))

        elif opc == "5":
            prefix = input("Prefixo do nome: ").strip()
            rows = filtrar_por_nome_inicio(prefix)
            if not rows:
                print("Nenhum cliente encontrado.")
            else:
                for r in rows:
                    print_cliente(r)

        elif opc == "6":
            try:
                cid = int(input("ID do cliente a atualizar: "))
                nome = input("Novo nome: ").strip()
                email = input("Novo email: ").strip()
                try:
                    ok = atualizar_cliente(cid, nome, email)
                    print("Atualizado." if ok else "ID não encontrado.")
                except ValueError as e:
                    print(e)
            except ValueError:
                print("ID inválido.")

        elif opc == "7":
            try:
                cid = int(input("ID do cliente a deletar: "))
                confirm = input("Confirmar exclusão? (s/N): ").strip().lower()
                if confirm == "s":
                    ok = deletar_cliente(cid)
                    print("Deletado." if ok else "ID não encontrado.")
                else:
                    print("Exclusão cancelada.")
            except ValueError:
                print("ID inválido.")

        elif opc == "0":
            print("Saindo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()

import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

print("✅ Tabela criada com sucesso!")

conexao.commit()
conexao.close()

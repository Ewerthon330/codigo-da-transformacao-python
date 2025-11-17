import csv
import shutil

arquivo = "notas.csv"
backup = "notas_backup.csv"

# --------- ADICIONAR NOTA ---------
nome = input("Nome do aluno: ")
disciplina = input("Disciplina: ")
nota = input("Nota: ")

with open(arquivo, "a", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow([nome, disciplina, nota])

print("\nNota salva com sucesso!")

# --------- CRIAR BACKUP ---------
shutil.copy(arquivo, backup)
print("Backup criado: notas_backup.csv")

# --------- LER O CSV ---------
print("\nConteúdo atual do arquivo:")
with open(arquivo, "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)

import csv

file = "notes.csv"

name = input("Students name: ")
discipline = input("Discipline")
note = input("Note:")

with open(file, "a", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow([name, discipline, note])

print("\nNota salva com sucesso!")

print("\nConteúdo do arquivo CSV:")

with open(file, "r", newline="", encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
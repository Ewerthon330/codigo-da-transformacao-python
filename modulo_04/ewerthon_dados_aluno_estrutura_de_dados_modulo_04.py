alunos = []

while True:

    aluno = {
        "nome": input("Digite o nome do aluno: "),
        "idade": int(input("Digite a idade: ")),
        "nota": float(input("Digite a nota: "))
    }

    alunos.append(aluno)

    continuar = input("Deseja adicionar outro aluno? (s/n): ").strip().lower()
    if continuar not in ("s", "sim"):
        break

print("\n--- Dados do Aluno ---")

for i, aluno in enumerate(alunos, start=1):
    print(f"\nAluno {i}:")
    for chave, valor in aluno.items():
        print(f"{chave.capitalize()}: {valor}")

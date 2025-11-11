def ler_notas_do_usuario(prompt="Insira as notas do aluno separadas por espaço: "):
    entrada = input(prompt).strip()
    if not entrada:
        return []  # lista vazia se o usuário não digitar nada
    partes = entrada.split()
    notas = []
    for p in partes:
        try:
            notas.append(float(p))
        except ValueError:
            # pula valores inválidos e avisa (pode-se também optar por falhar)
            print(f"Atenção: '{p}' não é uma nota válida e será ignorada.")
    return notas

def calcular_media(notas):
    if not notas:
        return None
    return sum(notas) / len(notas)

def verificar_aprovacao(media, limite=7.0):
    if media is None:
        return "Sem notas válidas para calcular a média."
    return "APROVADO" if media >= limite else "REPROVADO"

def main():
    notas = ler_notas_do_usuario()
    media = calcular_media(notas)
    if media is None:
        print("Não foi possível calcular média (nenhuma nota válida).")
        return

    status = verificar_aprovacao(media)
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")

if __name__ == "__main__":
    main()
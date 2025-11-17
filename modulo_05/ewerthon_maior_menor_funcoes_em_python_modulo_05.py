def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor


# --- Entrada do usuário ---
numeros = [int(x) for x in input("Digite números separados por espaço: ").split()]

maior, menor = maior_menor(numeros)

print("Maior número:", maior)
print("Menor número:", menor)

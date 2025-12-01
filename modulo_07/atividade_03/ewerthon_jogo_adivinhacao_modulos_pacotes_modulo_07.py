import random
import math

numero_secreto = random.randint(1, 100)
tentativas = 0

print("🎯 Jogo de Adivinhação (1 a 100)")

while True:
    chute = int(input("Digite um número: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")

# Apenas um uso simples de math:
raiz = math.sqrt(numero_secreto)
print(f"A raiz quadrada do número secreto era {raiz:.2f}")

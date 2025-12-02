n1 = int(input("Insert a number: "))
n2 = int(input("Insert other number: "))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

try:
    divisao = n1/n2
except ZeroDivisionError:
    print("Erro: Divisão por zero")
else:
    print(f"Result: {divisao}")
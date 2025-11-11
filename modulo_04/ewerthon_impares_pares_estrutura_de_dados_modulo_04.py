while True:
    numeros = [int(x) for x in input("Digite números separados por espaço: ").split()]

    pares = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    print("\nNúmeros pares:", pares)
    print("Números ímpares:", impares)

    repetir = input("\nDeseja digitar outros números? (s/n): ").strip().lower()
    if repetir not in ("s", "sim"):
        print("Encerrando o programa...")
        break

try:

    age = int(input("Whats your age?"))

    if age <= 0:
        print("The number cant be 0 or negative")
    else:
        print(f"Idade registrada: {age}")

except ValueError:
    print("Erro: Digite um ")

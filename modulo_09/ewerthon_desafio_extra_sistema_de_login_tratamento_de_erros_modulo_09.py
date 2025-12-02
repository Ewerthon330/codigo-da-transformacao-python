USERNAME = "admin"
PASSWORD = "1234"

for tentativa in range(3):
    try:
        user = input("Usuário: ")
        pwd = input("Senha: ")

        if user == USERNAME and pwd == PASSWORD:
            print("Login realizado com sucesso!")
            break
        else:
            raise ValueError("Credenciais inválidas!")

    except ValueError as e:
        print(e)
        print(f"Tentativas restantes: {2 - tentativa}")

else:
    print("Número máximo de tentativas atingido! Acesso bloqueado!")

import getpass  # usado para esconder a senha

# Dicionário para armazenar usuários e senhas
usuarios = {
    "admin": "1234"
}

def fazer_login():
    print("\n--- LOGIN ---")
    usuario = input("Usuário: ")
    senha = getpass.getpass("Senha: ")  # senha escondida

    if usuario in usuarios and usuarios[usuario] == senha:
        print("✔ Login realizado com sucesso!\n")
        return True
    else:
        print("❌ Usuário ou senha incorretos.\n")
        return False


def cadastrar_usuario():
    print("\n--- CADASTRAR NOVO USUÁRIO ---")
    novo_usuario = input("Digite o novo nome de usuário: ")

    if novo_usuario in usuarios:
        print("❌ Esse usuário já existe.\n")
        return

    nova_senha = getpass.getpass("Digite a nova senha: ")
    usuarios[novo_usuario] = nova_senha
    print("✔ Usuário cadastrado com sucesso!\n")


# ---------- MENU PRINCIPAL ----------
while True:
    print("=== MENU ===")
    print("1 - Login")
    print("2 - Cadastrar usuário")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tentativas = 3
        while tentativas > 0:
            if fazer_login():
                print("🎉 Bem-vindo ao sistema!\n")
                break
            else:
                tentativas -= 1
                print(f"Tentativas restantes: {tentativas}")

        if tentativas == 0:
            print("❌ Muitas tentativas inválidas. Voltando ao menu.\n")

    elif opcao == "2":
        cadastrar_usuario()

    elif opcao == "3":
        print("Encerrando o sistema... Até mais!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.\n")

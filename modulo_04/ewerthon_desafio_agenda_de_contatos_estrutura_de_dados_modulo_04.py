agenda = {}

while True:
    print("\nAgenda de Contatos")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar contatos")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone
    elif opcao == "2":
        nome = input("Nome para remover: ")
        if nome in agenda:
            del agenda[nome]
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Nome para buscar: ")
        if nome in agenda:
            print(f"{nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("\n--- Contatos ---")
        for nome, telefone in agenda.items():
            print(f"{nome}: {telefone}")
    elif opcao == "5":
        break
    else:
        print("Opção inválida!")

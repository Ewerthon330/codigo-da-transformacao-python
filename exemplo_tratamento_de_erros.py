def validar_id():
    try:
        id_usuario = input("Digite o ID do usuário: ")

        # tenta converter para inteiro
        id_int = int(id_usuario)

        # se for zero ou negativo, levantamos erro de propósito
        if id_int <= 0:
            raise ValueError("O ID deve ser maior que zero!")

        print(f"✅ ID {id_int} validado com sucesso!")

    except ValueError as erro:
        print(f"❌ Erro: {erro}\n O id deve ser apenas numérico")


# ======= chamada da função aqui =======    
validar_id()

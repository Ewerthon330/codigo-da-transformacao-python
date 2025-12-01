import json

ARQUIVO_DADOS = "clientes_data.json"

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "cidade": self.cidade}

class SistemaCadastro:
    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.clientes = self._carregar_dados()

    def _carregar_dados(self):
        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return [Cliente(**d) for d in dados]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def salvar_dados(self):
        dados_para_salvar = [cliente.to_dict() for cliente in self.clientes]
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(dados_para_salvar, f, indent=4, ensure_ascii=False)

    def adicionar_cliente(self, nome, idade, cidade):
        novo_cliente = Cliente(nome, idade, cidade)
        self.clientes.append(novo_cliente)
        self.salvar_dados()
        print(f"Cliente '{nome}' adicionado e dados salvos.")

    # aceite argumentos opcionais para manter compatibilidade com chamadas sem argumentos
    def atualizar_cliente(self, nome=None, idade=None, cidade=None):
        # se nome não foi passado, pede ao usuário
        if nome is None:
            nome = input("Digite o nome do cliente que deseja editar: ").strip()
            if not nome:
                print("Nome inválido. Operação cancelada.")
                return

        # encontra todos índices com o mesmo nome (case-insensitive)
        indices = [i for i, c in enumerate(self.clientes) if c.nome.lower() == nome.lower()]

        if not indices:
            print(f"Cliente '{nome}' não encontrado.")
            return

        # se há mais de um, deixa o usuário escolher
        if len(indices) > 1:
            print(f"Foram encontrados {len(indices)} clientes com o nome '{nome}':")
            for pos, idx in enumerate(indices, start=1):
                c = self.clientes[idx]
                print(f"{pos}. Nome: {c.nome}, Idade: {c.idade}, Cidade: {c.cidade}")
            while True:
                escolha = input("Escolha o número do cliente que deseja editar: ").strip()
                if escolha.isdigit() and 1 <= int(escolha) <= len(indices):
                    selecionado_idx = indices[int(escolha) - 1]
                    break
                print("Escolha inválida.")
        else:
            selecionado_idx = indices[0]

        cliente = self.clientes[selecionado_idx]
        print(f"Editando cliente: Nome: {cliente.nome}, Idade: {cliente.idade}, Cidade: {cliente.cidade}")

        # se idade/cidade/nome foram passados como argumentos, use-os; se None, pergunte ao usuário
        if nome is None:
            novo_nome = input("Novo nome (ENTER para manter): ").strip()
        else:
            # se o nome foi passado como argumento na chamada, já o usamos como novo_nome
            novo_nome = nome if nome != cliente.nome else ""
        if idade is None:
            nova_idade = input("Nova idade (ENTER para manter): ").strip()
        else:
            nova_idade = str(idade)
        if cidade is None:
            nova_cidade = input("Nova cidade (ENTER para manter): ").strip()
        else:
            nova_cidade = cidade if cidade != cliente.cidade else ""

        if novo_nome:
            cliente.nome = novo_nome
        if nova_idade:
            try:
                idade_int = int(nova_idade)
                if 0 < idade_int <= 150:
                    cliente.idade = idade_int
                else:
                    print("Idade inválida. Mantendo a idade anterior.")
            except ValueError:
                print("Idade inválida. Mantendo a idade anterior.")
        if nova_cidade:
            cliente.cidade = nova_cidade

        self.salvar_dados()
        print("Cliente atualizado com sucesso.")

    # aceite argumentos opcionais para manter compatibilidade com chamadas sem argumentos
    def remover_cliente(self, nome=None, idade=None, cidade=None):
        # se nome não foi passado, pede ao usuário
        if nome is None:
            nome = input("Digite o nome do cliente que deseja remover: ").strip()
            if not nome:
                print("Nome inválido. Operação cancelada.")
                return

        # encontra todos índices com o mesmo nome (case-insensitive)
        indices = [i for i, c in enumerate(self.clientes) if c.nome.lower() == nome.lower()]

        if not indices:
            print(f"Cliente '{nome}' não encontrado.")
            return

        # se há mais de um, deixa o usuário escolher
        if len(indices) > 1:
            print(f"Foram encontrados {len(indices)} clientes com o nome '{nome}':")
            for pos, idx in enumerate(indices, start=1):
                c = self.clientes[idx]
                print(f"{pos}. Nome: {c.nome}, Idade: {c.idade}, Cidade: {c.cidade}")
            while True:
                escolha = input("Escolha o número do cliente que deseja remover: ").strip()
                if escolha.isdigit() and 1 <= int(escolha) <= len(indices):
                    selecionado_idx = indices[int(escolha) - 1]
                    break
                print("Escolha inválida.")
        else:
            selecionado_idx = indices[0]

        cliente = self.clientes[selecionado_idx]
        confirm = input(f"Confirma remover '{cliente.nome}' (s/N)? ").strip().lower()
        if confirm == 's':
            # remove pelo índice para evitar problemas de igualdade de objetos
            del self.clientes[selecionado_idx]
            self.salvar_dados()
            print(f"Cliente '{cliente.nome}' removido com sucesso!")
        else:
            print("Operação cancelada.")

    def listar_clientes(self):
        if not self.clientes:
            print("\nNenhum cliente cadastrado.")
            return

        print("\n--- Lista de Clientes ---")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i}. Nome: {cliente.nome}, Idade: {cliente.idade}, Cidade: {cliente.cidade}")
        print("-------------------------")

def _obter_dados_cliente():
    print("\n--- Entrada de Dados ---")
    
    nome = input("Digite o Nome do Cliente: ").strip()
    if not nome:
        print("Nome não pode ser vazio. Operação cancelada.")
        return None, None, None

    while True:
        try:
            idade = int(input("Digite a Idade do Cliente: "))
            if 0 < idade <= 150:
                break
            print("Idade inválida.")
        except ValueError:
            print("Entrada inválida. Digite a idade usando apenas números inteiros.")

    cidade = input("Digite a Cidade do Cliente: ").strip()
    
    return nome, idade, cidade


def menu_principal():
    sistema = SistemaCadastro(ARQUIVO_DADOS)

    while True:
        print("\n=== Menu do Sistema de Clientes (POO) ===")
        print("1. Adicionar Novo Cliente")
        print("2. Listar Clientes Cadastrados")
        print("3. Editar Cliente")
        print("4. Remover Cliente")
        print("0. Sair do Sistema")
        
        opcao = input("Escolha uma opção (1, 2, 3, 4 ou 0): ").strip()
        
        if opcao == '1':
            nome, idade, cidade = _obter_dados_cliente()
            if nome:
                sistema.adicionar_cliente(nome, idade, cidade)

        elif opcao == '2':
            sistema.listar_clientes()

        elif opcao == '3':
            # mantive a chamada sem argumentos para respeitar sua estrutura original
            sistema.atualizar_cliente()

        elif opcao == '4':
            # mantive a chamada sem argumentos para respeitar sua estrutura original
            sistema.remover_cliente()
            
        elif opcao == '0':
            print("\nEncerrando o programa, até a próxima!")
            break
        else:
            print("Opção inválida. Por favor, digite 1, 2, 3, 4 ou 0.")

if __name__ == "__main__":
    menu_principal()

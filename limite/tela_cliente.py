from limite.tela import Tela

class TelaCliente(Tela):

    def tela_opcoes(self):
        print("-------- CADASTRO DE CLIENTES --------")
        print("1 -  Incluir novo cliente")
        print("2 -  Excluir  cliente")
        print("3 -  Listar  clientes")
        print("4 -  Alterar  um cliente")
        print("0 -  Voltar")
        opcao = self.verifica_opcao("Escolha uma opcão: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_cliente(self):
        print("----- DADOS CLIENTE -----")
        cpf = input("Cpf: ")
        nome = input("Nome: ")
        telefone = int(input("Telefone: "))
        idade = int(input("Idade: "))

        return {"cpf": cpf, "nome": nome, "telefone": telefone, "idade": idade}

    def pegar_dados_endereco(self):
        print("----- DADOS ENDEREÇO -----")
        rua = input("Digite o nome da rua: ")
        complemento = input("Digite o complemento: ")
        bairro = input("Digite o nome do bairro: ")
        cidade = input("Digite o nome da cidade: ")
        cep = input("Digite o cep da rua: ")

        return {"rua" : rua, "complemento" : complemento, "bairro" : bairro, "cidade" : cidade, "cep" : cep}

    def mostra_cliente(self, dados_cliente):
        if dados_cliente is not None:
            print("NOME: ", dados_cliente["nome"])
            print("CPF: ", dados_cliente["cpf"])
            print("TELEFONE: ", dados_cliente["telefone"])
            print("IDADE: ", dados_cliente["idade"])
            print("ENDEREÇOS: ")
            for i in dados_cliente["enderecos"]:
                print(f"Número: {i.numero}")
                print(f"Rua: {i.rua.capitalize()}")
                print(f"Complemento: {i.complemento.capitalize()}")
                print(f"Bairro: {i.bairro.capitalize()}")
                print(f"Cidade: {i.cidade.capitalize()}")
                print(f"Cep: {i.cep.capitalize()}")
                print("-"*10)
                print("CONTAS: ")
            for i in dados_cliente["contas"]:
                print("-"*10)
                print(f"Número: {i.numero}")
                print(f"Tipo: {i.tipo.name.capitalize()}")
                print(f"Funcionário: {i.funcionario.nome.capitalize()}")
                print(f"Saldo: {i.saldo:.2f}")

        else:
            print("Cliente não encontrado!")


    def seleciona_cliente(self):
        cpf_cliente = int(input(" CPF do cliente que deseja selecionar: "))

        return cpf_cliente

    def mostra_mensagem(self, msg):
        print(msg)
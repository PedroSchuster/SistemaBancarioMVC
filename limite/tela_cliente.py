from limite.tela import Tela

class TelaCliente(Tela):

    def tela_opcoes(self):
        print("-------- CADASTRO DE CLIENTES --------")
        print("1 -  Incluir novo cliente")
        print("2 -  Excluir  cliente")
        print("3 -  Listar  clientes")
        print("4 -  Buscar  um cliente")
        print("0 -  Voltar")
        opcao = self.verifica_opcao("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_cliente(self):
        print("----- DADOS CLIENTE -----")
        cpf = int(input("Cpf: "))
        nome = input("Nome: ")
        telefone = int(input("Telefone: "))
        idade = int(input("Idade: "))

        return {"cpf": cpf, "nome": nome, "telefone": telefone, "idade": idade}

    def mostra_cliente(self, dados_cliente):
        if dados_cliente is not None:
            print("NOME: ", dados_cliente["nome"])
            print("CPF: ", dados_cliente["cpf"])
            print("TELEFONE: ", dados_cliente["telefone"])
            print("IDADE: ", dados_cliente["idade"])

        else:
            print("Cliente não encontrado!")


    def seleciona_cliente(self):
        cpf_cliente = int(input(" CPF do cliente que deseja selecionar: "))

        return cpf_cliente

    def mostra_mensagem(self, msg):
        print(msg)
from limite.tela import Tela


class TelaFuncionario(Tela):

    def exibe_opcoes(self):
        print("-------- CADASTRO DE FUNCIONARIOS --------")
        print("1 -  Incluir novo funcionario")
        print("2 -  Excluir  funcionario")
        print("3 -  Listar  funcionarios")
        print("4 -  Buscar  um funcionario")
        print("0 -  Voltar")
        opcao = self.verifica_opcao("Escolha a opcao: ", [1, 2, 3, 4, 0])
        return opcao

    def pega_dados_funcionario(self):
        print("-------- DADOS FUNCIONARIO ----------")
        cpf = int(input("cpf: "))
        nome = input("nome: ")
        telefone = int(input("telefone"))
        matricula = int(input("matricula"))

        return {"cpf": cpf, "nome": nome, "telefone": telefone, "matricula": matricula}



    def mostra_funcionario(self, dados_funcionario):
        if dados_funcionario is not None:
            print("NOME: ", dados_funcionario["nome"])
            print("CPF: ", dados_funcionario["cpf"])
            print("TELEFONE: ", dados_funcionario["telefone"])

        else:
            print("Funcionario não encontrado!")

    def seleciona_funcionario(self):
        cpf_funcionario = int(input(" CPF do funcionario que deseja selecionar: "))

        return cpf_funcionario

    def mostra_mensagem(self, msg):
        print(msg)
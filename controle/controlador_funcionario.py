from entidade.funcionario import Funcionario
from limite.tela_funcionario import TelaFuncionario


class ControladorFuncionario:

    def __init__(self, controlador_sistema):
        self.__tela_funcionario = TelaFuncionario()
        self.__funcionario = []
        self.__controlador_sistema = controlador_sistema

    def inicia(self):
        self.tela_inicial()

    def pega_funcionario_por_cpf(self, cpf: int):
        for funcionario in self.__funcionario:
            if funcionario.cpf == cpf:
                return funcionario
        return None

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        funcionario = Funcionario(
            dados_funcionario["nome"],
            dados_funcionario["cpf"],
            dados_funcionario["telefone"],
            dados_funcionario["matricula"]
        )

        self.__funcionarios.append(funcionario)

    def excluir_funcionario(self):
        self.lista_funcionario()
        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        funcionario = self.pega_funcionario_por_cpf(cpf_funcionario)

        if funcionario is not None:
            self.__funcionario.remove(funcionario)
            self.lista_funcionario()
        else:
            self.__tela_funcionario.mostra_mensagem("funcionario não existente")

    def lista_funcionario(self):
        for funcionario in self.__funcionario:
            self.__tela_funcionario.mostra_funcionario({
                "nome": funcionario.nome,
                "cpf": funcionario.cpf,
                "telefone": funcionario.telefone,
                "matricula": funcionario.matricula})

    def buscar_funcionario(self):
        print("Buscar um funcionario ")

        matricula = int(input("Matricula do funcionario: "))
        for funcionario in self.__funcionario:
            if Funcionario.matricula == matricula:
                return funcionario
            return "Funcionario não encontrado"

    def tela_inicial(self):
        caso = {0: self.retornar, 1: self.incluir_funcionario, 2: self.excluir_funcionario,
                3: self.lista_funcionario, 4: self.buscar_funcionario}

        while True:
            opcao = self.__tela_funcionario.exibe_opcoes()
            opcao_escolhida = caso[opcao]
            opcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abre_tela()
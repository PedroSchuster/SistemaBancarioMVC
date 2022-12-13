from entidade.funcionario import Funcionario
from limite.tela_funcionario import TelaFuncionario


class ControladorFuncionario:

    def __init__(self, controlador_sistema):
        self.__funcionario = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_funcionario = TelaFuncionario()
        self.__dao = controlador_sistema.dao

    def pega_funcionario_por_cpf(self, cpf):
        self.__funcionario = self.__dao.get_list('funcionarios')
        for i in range(len(self.__funcionario)):
            if self.__funcionario[i].cpf == cpf:
                return i
        return None

    def incluir_funcionario(self):
        dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
        funcionario = Funcionario(dados_funcionario["nome"], dados_funcionario["cpf"], dados_funcionario["telefone"],
                         dados_funcionario["matricula"])

        self.__dao.add('funcionarios', funcionario)

        #self.__funcionario.append(funcionario)

    def excluir_funcionario(self):
        self.lista_funcionario()
        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        index = self.pega_funcionario_por_cpf(cpf_funcionario)

        if index is not None:
            self.__dao.remove(index, 'funcionarios')
            self.lista_funcionario()
        else:
            self.__tela_funcionario.mostra_mensagem("funcionario não existente")

    def alterar_funcionario(self):
        self.lista_funcionario()
        cpf_funcionario = self.__tela_funcionario.seleciona_funcionario()
        index = self.pega_funcionario_por_cpf(cpf_funcionario)

        if index is not None:
            novos_dados_funcionario = self.__tela_funcionario.pega_dados_funcionario()
            funcionario = Funcionario(novos_dados_funcionario["nome"], 
            novos_dados_funcionario["telefone"], novos_dados_funcionario["cpf"],novos_dados_funcionario["matricula"])
            self.__dao.modify(index, 'funcionarios', funcionario)
            self.lista_clientes()
        else:
             self.__tela_funcionario.mostra_mensagem("funcionario nã existente")

    def lista_funcionario(self):
        self.__funcionario = self.__dao.get_list('funcionarios')
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

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_funcionario, 2: self.excluir_funcionario, 3: self.lista_funcionario,
                        4: self.alterar_funcionario,
                        0: self.retornar}
                
        continua = True

        while continua:
            lista_opcoes[self.__tela_funcionario.exibe_opcoes()]()
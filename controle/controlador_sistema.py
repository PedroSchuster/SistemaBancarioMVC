import sys
from controle.controlador_cliente import ControladorCliente
from controle.controlador_funcionario import ControladorFuncionario
from controle.controlador_conta import ControladorConta
from controle.controlador_operacao import ControladorOperacao
from excecoes.valor_invalido_exception import ValorInvalidoException
from limite.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_operacao = ControladorOperacao(self)
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__tela = TelaSistema()

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    def inicializa_sistema(self):
        opcoes = {1: self.cadastrar_clientes, 2: self.cadastrar_funcionarios,
                  3: self.cadastrar_contas, 4: self.abrir_operacoes}
        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao == 0:
                    sys.exit()

                opcoes[opcao]()

            except ValueError:
                self.__tela.mostrar_mensagem(
                    "Valor inválido, verifique se o tipo do valor da entrada está correto!")
            except ValorInvalidoException as e:
                self.__tela.mostrar_mensagem(e.mensagem)
            except Exception as e:
                self.__tela.mostrar_mensagem(e.args[0])

    def cadastrar_contas(self):
        self.__controlador_conta.abre_tela()

    def cadastrar_clientes(self):
        self.__controlador_cliente.abre_tela()

    def cadastrar_funcionarios(self):
        self.__controlador_funcionario.abre_tela()

    def abrir_operacoes(self):
        self.__controlador_operacao.abre_tela()
        

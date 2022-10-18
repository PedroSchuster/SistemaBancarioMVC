import sys
from controlador_cliente import ControladorCliente
from controlador_funcionario import ControladorFuncionario
from controlador_conta import ControladorConta
from controlador_operacao import ControladorOperacao
from excecoes.valor_invalido_exception import ValorInvalidoException
from limite.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_operacao = ControladorOperacao(self)
        self.__controlador_conta = ControladorConta(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__tela = TelaSistema()
        
    def inicializa_sistema(self):
        opcoes = {1:self.cadastrar_clientes, 2:self.cadastrar_funcionarios, 3 : self.cadastrar_contas, 4: self.abrir_operacoes}
        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                if opcao == 0:
                    sys.exit()
                    
                opcoes[opcao]()        
            except ValueError:
                self.__tela.mostrar_mensagem(["Valor inválido, digite um numero inteiro"])
            except ValorInvalidoException as e:
                self.__tela.mostrar_mensagem([e.mensagem])
                
    def cadastrar_contas(self):
        self.__controlador_conta.abre_tela()
    
    def cadastrar_clientes(self):
        self.__controlador_cliente.abre_tela()
    
    def cadastrar_funcionarios(self):
        self.__controlador_funcionario.abre_tela()
    
    def abrir_operacoes(self):
        pass

iniciar = ControladorSistema()
iniciar.inicializa_sistema()
        
import sys
from controlador_conta import ControladorConta
from controlador_operacao import ControladorOperacao
from Excecoes.valor_invalido_exception import ValorInvalidoException
from Limite.tela_sistema import TelaSistema

class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_operacao = ControladorOperacao(self)
        self.__controlador_conta = ControladorConta(self)
        self.__tela = TelaSistema()
        
    def inicializa_sistema(self):
        opcoes = {1:self.cadastrar_contas, 2:self.abrir_operacoes}
        while True:
            try:
                opcao = self.__tela.tela_opcoes
                if opcao == 0:
                    sys.exit()
                    
                opcoes[opcao]()        
            except ValueError:
                self.__tela.mostrar_mensagem(["Valor inválido, digite um numero inteiro"])
            except ValorInvalidoException as e:
                self.__tela.mostrar_mensagem([e.mensagem])
                
    def cadastrar_contas(self):
        self.__controlador_conta.abre_tela()
        
    def abrir_operacoes(self):
        pass
        
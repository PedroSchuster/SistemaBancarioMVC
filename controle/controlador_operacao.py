from datetime import datetime
from limite.tela_operacao import TelaOperacao
from excecoes.valor_invalido_exception import ValorInvalidoException
from entidade.operacao import Operacao

class ControladorOperacao:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaOperacao
    
    def transacao(self):
        conta_origem = self.__controlador_sistema.controlador_conta.pegar_contar_por_numero(self.__tela.selecionar_conta())
        dados_operacao = self.__tela.pegar_dados_operacao()
        conta_destino = self.__controlador_sistema.controlador_conta.pegar_contar_por_numero(dados_operacao["conta_destino"])
        valor = dados_operacao["valor"]
        
        if (valor < conta_destino.saldo):
            raise ValorInvalidoException(valor)
        
        
        operacao_origem = Operacao(datetime.now.__reduce__, "Transação", valor)
        operacao_destino = Operacao(datetime.now.__reduce__, "Transação", -valor)
        
        conta_origem.operacoes.append(operacao_origem)
        conta_destino.operacoes.append(operacao_destino)
        
        conta_origem.saldo -= valor
        conta_destino.saldo += valor

        self.__controlador_sistema.controlador_conta.registrar_operacao(conta_origem, )
        self.__tela.mostrar_mensagem(["Transacao feito com sucesso!", f"Novo saldo da conta {conta_origem} é {conta_origem.saldo}"])
    
    def saque(self):
        conta_origem = self.__controlador_sistema.controlador_conta.pegar_contar_por_numero(self.__tela.selecionar_conta())
        valor = self.__tela.pegar_dado_saque()
        
        if (valor > conta_origem.saldo):
            raise ValorInvalidoException(valor)
        
        conta_origem.saldo -= valor 
        self.__tela.mostrar_mensagem(["Saque feito com sucesso!", f"Novo saldo da conta {conta_origem} é {conta_origem.saldo}"])
    
    def deposito(self):
        conta_origem = self.__controlador_sistema.controlador_conta.pegar_contar_por_numero(self.__tela.selecionar_conta())
        valor = self.__tela.pegar_dado_saque()
        
        if (valor > conta_origem.saldo):
            raise ValorInvalidoException(valor)
        
        conta_origem.saldo += valor 
        self.__tela.mostrar_mensagem(["Depósito feito com sucesso!", f"Novo saldo da conta {conta_origem} é {conta_origem.saldo}"])
        
    
    def abre_tela(self):
        opcoes = {1:self.transacao, 2: self.saque, 3: self.deposito}
        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                
                if opcao == 0:
                    break

                opcoes[opcao]()  
            except ValueError:
                self.__tela_conta.mostrar_mensagem(["Valor inválido, digite um numero inteiro"])
            except ValorInvalidoException as e:
                self.__tela_conta.mostrar_mensagem([e.mensagem])
 

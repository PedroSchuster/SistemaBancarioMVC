from datetime import datetime
from dao.dao_main import DAO
from enums.tipo_conta import TipoConta
from enums.tipo_operacao import TipoOperacao
from excecoes.operacao_exception import OperacaoException
from limite.tela_operacao import TelaOperacao
from excecoes.valor_invalido_exception import ValorInvalidoException
from excecoes.cadastro_exception import CadastroException
from entidade.operacao import Operacao

class ControladorOperacao:
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela = TelaOperacao()
        self.__dao = DAO('operacoes.pkl')

    
    def transacao(self):
        index_origem = self.__controlador_sistema.controlador_conta.listar_contas()
        conta_origem = self.__dao.get_one(index_origem, "contas")

        if (not conta_origem):
            raise CadastroException("Conta de origem não encontrada")
        elif (conta_origem.tipo == TipoConta.poupanca):
            raise CadastroException("Não é possivel fazer transações com conta do tipo poupança")

        index_destino = self.__controlador_sistema.controlador_conta.listar_contas()
        conta_destino = self.__dao.get_one(index_destino, "contas")

        if (not conta_destino):
            raise CadastroException("Conta de destino não encontrada")
        elif (conta_destino.tipo == TipoConta.poupanca):
            raise OperacaoException("Não é possivel fazer transações com conta do tipo poupança")
        elif (conta_origem.numero == conta_destino.numero):
            raise OperacaoException("Não é possivel fazer transações entre duas contas iguais")
        
        valor = self.__tela.pegar_valor()
       
        if (valor > conta_origem.saldo):
            raise OperacaoException(f"A conta {conta_origem.numero} não possui saldo suficiente")
        
        conta_origem.saldo -= valor
        conta_destino.saldo += valor

        operacao_origem = Operacao(datetime.now(), TipoOperacao.transacao, -valor)
        operacao_destino = Operacao(datetime.now(), TipoOperacao.transacao, valor)
        
        self.registrar_operacao(operacao_origem, conta_origem, index_origem)
        self.registrar_operacao(operacao_destino, conta_destino, index_destino)

        self.__tela.mostrar_mensagem("Transacao feito com sucesso! ")
        self.__tela.mostrar_mensagem(f"Novo saldo da conta {conta_origem.numero} é {conta_origem.saldo:.2f}")
        self.__tela.mostrar_mensagem(f"Novo saldo da conta {conta_destino.numero} é {conta_destino.saldo:.2f}")
    
    def saque(self):
        index_origem = self.__controlador_sistema.controlador_conta.listar_contas()
        conta_origem = self.__dao.get_one(index_origem, "contas")

        if (not conta_origem):
            raise CadastroException("Conta de origem não encontrada")

        valor = self.__tela.pegar_valor()

        if (valor > conta_origem.saldo):
            raise OperacaoException(f"A conta {conta_origem.numero} não possui saldo suficiente")

        conta_origem.saldo -= valor 
        self.__dao.modify(index_origem, "contas", conta_origem)
        
        operacao_origem = Operacao(datetime.now(), TipoOperacao.saque, -valor)
        self.registrar_operacao(operacao_origem, conta_origem, index_origem)

        self.__tela.mostrar_mensagem("Saque feito com sucesso! ")
        self.__tela.mostrar_mensagem(f"Novo saldo da conta {conta_origem.numero} é {conta_origem.saldo:.2f}")
    
    def deposito(self):
        index_origem = self.__controlador_sistema.controlador_conta.listar_contas()
        conta_origem = self.__dao.get_one(index_origem, "contas")

        if (not conta_origem):
            raise CadastroException("Conta de origem não encontrada")

        valor = self.__tela.pegar_valor()
        conta_origem.saldo += valor 
        
        operacao_origem = Operacao(datetime.now(), TipoOperacao.deposito, valor)
        self.registrar_operacao(operacao_origem, conta_origem, index_origem)

        self.__tela.mostrar_mensagem("Depósito feito com sucesso! ")
        self.__tela.mostrar_mensagem(f"Novo saldo da conta {conta_origem.numero} é {conta_origem.saldo:.2f}")
    
    def extrato(self):
        index_origem = self.__controlador_sistema.controlador_conta.listar_contas()
        conta_origem = self.__dao.get_one(index_origem, "contas")

        if (not conta_origem):
            raise CadastroException("Conta de origem não encontrada")

        self.__tela.mostrar_extrato(conta_origem.operacoes)
    
    def consulta_saldo(self):
        index_origem = self.__controlador_sistema.controlador_conta.listar_contas()
        conta_origem = self.__dao.get_one(index_origem, "contas")

        if (not conta_origem):
            raise CadastroException("Conta de origem não encontrada")
            
        self.__tela.mostrar_saldo(conta_origem)


    def registrar_operacao(self, operacao, conta, index):
        conta.add_operacao(operacao)
        self.__dao.modify(index, "contas", conta)


    def abre_tela(self):
        opcoes = {1:self.transacao, 2: self.saque, 3: self.deposito, 4: self.extrato, 5 : self.consulta_saldo}
        while True:
            try:
                opcao = self.__tela.tela_opcoes()
                
                if opcao == 0:
                    break

                opcoes[opcao]()  
            except ValueError:
                self.__tela.mostrar_mensagem("Valor inválido, verifique se o tipo do valor da entrada está correto!")
            except AttributeError:
                self.__tela.mostrar_mensagem("Tipo de operação não encontrado!")
            except ValorInvalidoException as e:
                self.__tela.mostrar_mensagem(e.mensagem)
            except CadastroException as e:
                self.__tela.mostrar_mensagem(e.mensagem)
            except OperacaoException as e:
                self.__tela.mostrar_mensagem(e.mensagem)
                
 

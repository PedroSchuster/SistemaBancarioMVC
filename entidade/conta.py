from entidade.cliente import Cliente
from entidade.funcionario import Funcionario
from enums.tipo_conta import TipoConta
from enums.tipo_operacao import TipoOperacao


class Conta:
    
    def __init__(self, numero : int, tipo : TipoConta, cliente : Cliente, funcionario : Funcionario):
        self.__numero = numero
        self.__saldo = 0
        self.__tipo = tipo
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.__operacoes = []
        
    @property 
    def numero(self):
        return self.__numero
        
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
            
    @property
    def saldo(self):
        return self.__saldo
        
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
        
    @property
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
        
    @property
    def cliente(self):
        return self.__cliente
        
    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def funcionario(self):
        return self.__funcionario
        
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario

    @property
    def operacoes(self):
        return self.__operacoes
        
    def add_operacao(self, operacao):
        self.__operacoes.append(operacao)
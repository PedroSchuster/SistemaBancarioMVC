class Conta:
    
    def __init__(self, numero, tipo, cliente, funcionario):
        self.__numero = numero
        self.__saldo = 0
        self.__tipo = tipo
        self.__cliente = cliente
        self.__funcionario = funcionario
        self.operacoes = []
        
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
        
    @property
    def funcionario(self):
        return self.__funcionario
        
    @funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario
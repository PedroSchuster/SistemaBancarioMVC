class Operacao:
    
    def __init__(self, data_operacao, tipo, valor):
        self.__data_operacao = data_operacao
        self.__tipo = tipo
        self.__valor = valor
        
    @property
    def data_operacao(self):
        return self.__data_operacao
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def valor(self):
        return self.__valor
    
    
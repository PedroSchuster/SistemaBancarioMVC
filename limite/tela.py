from abc import ABC, abstractmethod
from excecoes.valor_invalido_exception import ValorInvalidoException

class Tela(ABC):
    
    
    def verifica_opcao(self,mensagem, inteiros_validos):
        while True:
            valor_inserido = int(input(mensagem))
            if valor_inserido in inteiros_validos:
                return valor_inserido
            else:
                raise ValorInvalidoException(valor_inserido)
            
    
    def mostrar_mensagem(self,mensagens):
        for i in mensagens:
            print(i)
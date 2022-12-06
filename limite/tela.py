from abc import ABC, abstractmethod
from excecoes.valor_invalido_exception import ValorInvalidoException
import PySimpleGUI as sg

class Tela(ABC):
    
    def verifica_opcao(self,mensagem, inteiros_validos):
        while True:
            valor_inserido = int(input(mensagem))
            if valor_inserido in inteiros_validos:
                return valor_inserido
            else:
                raise ValorInvalidoException(valor_inserido)
            
    def pegar_opcao(self, botao, inteiros_validos):
        for k,v in inteiros_validos.items():
            if (v):
                return int(k)
        if inteiros_validos['0'] or botao in (None, 'Cancelar'):
            return 0
    
    def mostrar_mensagem(self,mensagem):
        sg.Popup('-------- AVISO ----------', mensagem)


    def tela_opcoes(self):
        return self.mostrar_mensagem("Tela não encontrada")
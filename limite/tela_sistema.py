from limite.tela import Tela
import PySimpleGUI as sg 


class TelaSistema(Tela):
    
    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('DarkTeal4')

    def tela_opcoes(self):
        layout = [
      [sg.Text("-------- CADASTRO DE CONTAS --------", font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio("Cliente", "RD1", key='1')],
      [sg.Radio("Funcionário", "RD1", key='2')],
      [sg.Radio("Conta", "RD1", key='3')],
      [sg.Radio("Operações", "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        opcao = self.pegar_opcao(button, values)
        self.close()
        return opcao

    def pegar_opcao(self, botao, inteiros_validos):
        return super().pegar_opcao(botao, inteiros_validos)
    
    def mostrar_mensagem(self,mensagem):
        return super().mostrar_mensagem(mensagem)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
from enums.tipo_conta import TipoConta
from limite.tela import Tela
import PySimpleGUI as sg


class TelaConta(Tela):

    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('DarkTeal4')

    def tela_opcoes(self):
        layout = [
      [sg.Text("-------- CADASTRO DE CONTAS --------", font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio("Cadastrar conta", "RD1", key='1')],
      [sg.Radio("Alterar cadastro", "RD1", key='2')],
      [sg.Radio("Excluir cadastro", "RD1", key='3')],
      [sg.Radio("Listar contas", "RD1", key='4')],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        opcao = self.pegar_opcao(button, values)
        self.close()
        return opcao

    def mostrar_conta(self, conta):
        resultado = ''
        resultado += f"Número: {conta.numero}" + '\n'
        resultado += f"Tipo: {conta.tipo.name.capitalize()}" '\n'
        resultado += f"Cliente: {conta.cliente.nome.capitalize()}" + '\n'
        resultado += f"Funcionário: {conta.funcionario.nome.capitalize()}" '\n'
        resultado += f"Saldo: {conta.saldo:.2f}" + '\n'
        sg.Popup('-------- VISUALIZAR CONTA ----------', resultado)

    def listar_contas(self, list):
        layout = [[sg.Text('Choose additional Facilities',size=(30, 1), font='Lucida',justification='left')],
         [sg.Listbox(values=list, key='conta', size=(30, 6))],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]]

        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        self.close()
        
        if button == 'Cancelar':
            return None

        return values['conta'][0]


    def pegar_dados_conta(self):
        layout = [
      [sg.Text('-------- DADOS DA CONTA ----------', font=("Helvica", 25))],
      [sg.Text('Numero da conta::', size=(15, 1)), sg.InputText('', key='numero')],
      [sg.Text('Tipo da conta::', size=(15, 1))],
      [sg.Combo(['corrente', 'poupanca'], default_value='corrente', key='tipo')],
      [sg.Text('Cpf do cliente: :', size=(15, 1)), sg.InputText('', key='cliente')],
      [sg.Text('Cpf do funcionario::', size=(15, 1)), sg.InputText('', key='funcionario')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]

        self.__window = sg.Window('Sistema de livros').Layout(layout)
        button, values = self.open()
        self.close()

        if button == 'Cancelar':
            return None
        return values
        
    
    def mostrar_mensagem(self,mensagem):
        return super().mostrar_mensagem(mensagem)
    
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
from limite.tela import Tela
import PySimpleGUI as sg

class TelaOperacao(Tela):

    def __init__(self):
        self.__window = None
        sg.ChangeLookAndFeel('DarkTeal4')
   
    def mostrar_mensagem(self, mensagem):
        return super().mostrar_mensagem(mensagem)
    
    def tela_opcoes(self):
        layout = [
      [sg.Text("-------- SELECIONAR OPERAÇÃO --------", font=("Helvica", 25))],
      [sg.Text('Escolha sua opção', font=("Helvica", 15))],
      [sg.Radio("Transação", "RD1", key='1')],
      [sg.Radio("Saque", "RD1", key='2')],
      [sg.Radio("Deposito", "RD1", key='3')],
      [sg.Radio("Extrato", "RD1", key='4')],
      [sg.Radio("Saldo", "RD1", key=5)],
      [sg.Radio('Retornar', "RD1", key='0')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        opcao = self.pegar_opcao(button, values)
        self.close()
        return opcao

    def selecionar_conta(self):
        layout = [
        [sg.Text("-------- SELECIONAR CONTA --------", font=("Helvica", 25))],
        [sg.Text('Número da conta: ', font=("Helvica", 15)), sg.InputText('', key='numero')]]

        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        self.close()
        
        if button == 'Cancelar':
            return None
        return int(values['numero'])
    
    def pegar_valor(self):
        layout = [
        [sg.Text("-------- SELECIONAR VALOR --------", font=("Helvica", 25))],
        [sg.Text('Insira o valor: ', font=("Helvica", 15)), sg.InputText('', key='valor')]]

        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        self.close()
        
        if button == 'Cancelar':
            return None
        return int(values['valor'])
    
    def selecionar_conta_destino(self):
        layout = [
        [sg.Text("-------- SELECIONAR CONTA DESTINO --------", font=("Helvica", 25))],
        [sg.Text('Número da conta de destino: ', font=("Helvica", 15)), sg.InputText('', key='numero')]]

        self.__window = sg.Window('Sistema bancario').Layout(layout)
        button, values = self.open()
        self.close()
        
        if button == 'Cancelar':
            return None
        return int(values['numero'])
    
    def mostrar_saldo(self, conta):
        return self.mostrar_mensagem(f"Saldo: {conta.saldo:.2f}")

    def mostrar_mensagem(self, mensagem):
        return super().mostrar_mensagem(mensagem)

    def mostrar_extrato(self, dados_extrato):
        
        for i in dados_extrato:
            resultado = ''
            resultado += f"Tipo {i.tipo.name.capitalize()}" + '\n'
            resultado += f"Valor: {i.valor:.2f}" '\n'
            resultado += f"Data: {i.data_operacao.strftime('%d/%m/%Y %H:%M')}" + '\n'
        sg.Popup('-------- VISUALIZAR CONTA ----------', resultado)
    
    def pegar_opcao(self, botao, inteiros_validos):
        return super().pegar_opcao(botao, inteiros_validos)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
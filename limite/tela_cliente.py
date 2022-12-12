from limite.tela import Tela
import PySimpleGUI as sg 

class TelaCliente(Tela):

    def tela_opcoes(self):

        layout = [
                        [sg.Text('CADASTRO DE CLIENTES', font=("Helvica",25))],
                        [sg.Text('Escolha sua opção:', font=("Helvica",15))],
                        [sg.Radio('Incluir novo cliente',"RD1", key='1')],
                        [sg.Radio('Excluir  cliente',"RD1", key='2')],
                        [sg.Radio('Listar clientes',"RD1", key='3')],
                        [sg.Radio('Voltar',"RD1", key='0')],
                        [sg.Button('Confirmar'), sg.Cancel('Cancelar',key='0')]
                    ]
        __window = sg.Window('Clientes').Layout(layout)
        button, values = __window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        #cobre casos
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0

        __window.close()
        return opcao

    def pega_dados_cliente(self):

        layout = [
                        [sg.Text('DADOS DO CLIENTE', font=("Helvica",25))],
                        [sg.Text('Nome', size =(15, 1)), sg.InputText()],
                        [sg.Text('CPF', size =(15, 1)), sg.InputText()],                        
                        [sg.Text('Telefone', size =(15, 1)), sg.InputText()],
                        [sg.Text('Idade', size =(15, 1)), sg.InputText()],
                        [sg.Button('Confirmar'), sg.Cancel('Cancelar',key='0')]
                    ]
        __window = sg.Window('Cadastrar').Layout(layout)
        
        button, values = __window.Read()
        __window.close()
        return {"cpf": values[1], "nome": values[0], "telefone": values[2], "idade": values[3]}


    def pegar_dados_endereco(self):
        print("----- DADOS ENDEREÇO -----")
        rua = input("Digite o nome da rua: ")
        complemento = input("Digite o complemento: ")
        bairro = input("Digite o nome do bairro: ")
        cidade = input("Digite o nome da cidade: ")
        cep = input("Digite o cep da rua: ")

        return {"rua" : rua, "complemento" : complemento, "bairro" : bairro, "cidade" : cidade, "cep" : cep}

    def mostra_cliente(self, dados_cliente):
        if dados_cliente is not None:

            layout = [
                            [sg.Text('NOME: '+dados_cliente["nome"])],
                            [sg.Text('CPF: '+dados_cliente["cpf"])],
                            [sg.Text('TELEFONE: '+dados_cliente["telefone"])],
                            [sg.Text('IDADE: '+dados_cliente["idade"])],

                            [sg.Button('OK',key='0')]
                        ]
            __window = sg.Window('Mostrar Cliente').Layout(layout)
                
            button, values = __window.Read()
            __window.close()    


        else:

            layout = [
                            [sg.Text('Cliente não encontrado!')],
                            [sg.Button('OK',key='0')]
                        ]
            __window = sg.Window('Mostrar Carro').Layout(layout)
                
            button, values = __window.Read()
            __window.close()
            

    def seleciona_cliente(self):

        layout = [
                        [sg.Text('CPF do cliente que deseja selecionar:', size =(15, 1)), sg.InputText()],
                        [sg.Button('Confirmar'), sg.Cancel('Cancelar',key='0')]
                    ]
        __window = sg.Window('Alterar').Layout(layout)
            
        button, values = __window.Read()
        __window.close()
        return values[0]
        

    def mostra_mensagem(self, msg):

        layout = [
                            [sg.Text(msg)],

                            [sg.Button('OK',key='0')]
                   ]
        __window = sg.Window('Informações').Layout(layout)
                
        button, values = __window.Read()
        __window.close()
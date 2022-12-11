from limite.tela import Tela
import PySimpleGUI as sg


class TelaFuncionario(Tela):

    def exibe_opcoes(self):

        layout = [
                        [sg.Text('CADASTRO DE FUNCIONARIOS', font=("Helvica",25))],
                        [sg.Text('Escolha sua opção:', font=("Helvica",15))],
                        [sg.Radio('Incluir novo funcionario',"RD1", key='1')],
                        [sg.Radio('Excluir  funcionario',"RD1", key='2')],
                        [sg.Radio('Listar  funcionarios',"RD1", key='3')],
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
           
        # cobre os casos de voltar, não clicar em nada e fechar janela, ou clicar cancelar
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0

        __window.close()  
        """print("-------- CADASTRO DE FUNCIONARIOS --------")
        print("1 -  Incluir novo funcionario")
        print("2 -  Excluir  funcionario")
        print("3 -  Listar  funcionarios")
        print("4 -  Alterar  um funcionario")
        print("0 -  Voltar")
        opcao = self.verifica_opcao("Escolha uma opcão: ", [1, 2, 3, 4, 0])"""
        return opcao

    def pega_dados_funcionario(self):

        layout = [
                        [sg.Text('DADOS DO FUNCIONARIO', font=("Helvica",25))],
                        [sg.Text('Nome', size =(15, 1)), sg.InputText()],
                        [sg.Text('CPF', size =(15, 1)), sg.InputText()],                        
                        [sg.Text('Telefone', size =(15, 1)), sg.InputText()],
                        [sg.Text('Matricula', size =(15, 1)), sg.InputText()],
                        [sg.Button('Confirmar'), sg.Cancel('Cancelar',key='0')]
                    ]
        __window = sg.Window('Cadastrar').Layout(layout)
        
        button, values = __window.Read()
        __window.close()
        """print("-------- DADOS FUNCIONARIO ----------")
        cpf = input("cpf: ")
        nome = input("nome: ")
        telefone = int(input("telefone:"))
        matricula = int(input("matricula:"))"""

        #return {"cpf": cpf, "nome": nome, "telefone": telefone, "matricula": matricula}
        return {"cpf": values[1], "nome": values[0], "telefone": values[2], "matricula": values[3]}



    def mostra_funcionario(self, dados_funcionario):
        if dados_funcionario is not None:
            layout = [
                            [sg.Text('NOME: '+dados_funcionario["nome"])],
                            [sg.Text('CPF: '+dados_funcionario["cpf"])],
                            [sg.Text('TELEFONE: '+dados_funcionario["telefone"])],

                            [sg.Button('OK',key='0')]
                        ]
            __window = sg.Window('Mostrar Funcionario').Layout(layout)
                
            button, values = __window.Read()
            __window.close()    
        else:

            layout = [
                            [sg.Text('Funcionario não encontrado!')],
                            [sg.Button('OK',key='0')]
                        ]
            __window = sg.Window('Mostrar Carro').Layout(layout)
                
            button, values = __window.Read()
            __window.close()
            """print("NOME: ", dados_funcionario["nome"])
            print("CPF: ", dados_funcionario["cpf"])
            print("TELEFONE: ", dados_funcionario["telefone"])

        else:
            print("Funcionario não encontrado!")"""

    def seleciona_funcionario(self):

        layout = [
                        [sg.Text('CPF do funcionario que deseja selecionar:', size =(15, 1)), sg.InputText()],
                        [sg.Button('Confirmar'), sg.Cancel('Cancelar',key='0')]
                    ]
        __window = sg.Window('Alterar').Layout(layout)
            
        button, values = __window.Read()
        __window.close()    
        return values[0]
        #cpf_funcionario = input(" CPF do funcionario que deseja selecionar: ")

        #return cpf_funcionario

    def mostra_mensagem(self, msg):

        layout = [
                        [sg.Text(msg)],

                        [sg.Button('OK',key='0')]
                ]
        __window = sg.Window('Informações').Layout(layout)
                
        button, values = __window.Read()
        __window.close()
        #print(msg)
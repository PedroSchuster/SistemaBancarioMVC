from limite.tela import Tela

class TelaOperacao(Tela):
    
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def mostrar_mensagem(self, mensagens):
        return super().mostrar_mensagem(mensagens)
    
    def tela_opcoes(self):
        print("*"*10)
        print("1 - Transação")
        print("2 - Saque")
        print("3 - Deposito")
        print("4 - Extrato")
        print("5 - Saldo")
        print("0 - Encerrar")
        opcao = self.verifica_opcao("Escolhe uma opção: ", [1,2,3,4,5,0])
        return opcao
    
    def selecionar_conta(self):
        return input("Digite o numero da conta: ")
    
    def pegar_dado_saque(self):
        return input("Digite o valor a ser sacado")
    
    
    def pegar_dados_operacao(self):
        dados_operacao = {}
        dados_operacao["conta_destino" : int(input("Digite o numero da conta de destino: "))]
        dados_operacao["valor" : float(input("Digite o valor a ser transferido: "))]
        return dados_operacao
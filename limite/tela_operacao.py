from tela import Tela

class TelaOperacao(Tela):
    
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def mostrar_mensagem(self, mensagens):
        return super().mostrar_mensagem(mensagens)
    
    def selecionar_conta(self):
        pass
        
    def tela_opcoes(self):
        print("*"*10)
        print("1 - Transação")
        print("2 - Saque")
        print("3 - Deposito")
        print("4 - Extrato")
        print("5 - Saldo")
        print("0 - Encerrar")
        opcao = self.verifica_opcao("ESCOLHA UMA OPÇÃO: ", [1,2,3,4,0])
        return opcao
    
    def pegar_dados_operacao():
        pass
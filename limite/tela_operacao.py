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
        print("0 - Retornar")
        opcao = self.verifica_opcao("Escolhe uma opção: ", [1,2,3,4,5,0])
        return opcao
    
    def selecionar_conta(self):
        return int(input("Digite o numero da conta: "))
    
    def pegar_valor(self):
        return float(input("Digite o valor: "))
    
    
    def selecionar_conta_destino(self):
        return int(input("Digite o numero da conta de destino: "))
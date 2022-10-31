from limite.tela import Tela

class TelaOperacao(Tela):
    
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def mostrar_mensagem(self, mensagem):
        return super().mostrar_mensagem(mensagem)
    
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
    
    def mostrar_saldo(self, conta):
        print(f"Saldo: {conta.saldo: .2f }")

    def mostrar_extrato(self, dados_extrato):
        print("-"*10)
        for i in dados_extrato:
            print(f"Tipo {i.tipo.name.capitalize()}")
            print(f"Valor: {i.valor :.2f}")
            print(f"Data: {i.data_operacao.strftime('%d/%m/%Y %H:%M')}")
            print("-"*10)

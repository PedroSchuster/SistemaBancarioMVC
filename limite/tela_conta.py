from limite.tela import Tela


class TelaConta(Tela):
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def tela_opcoes(self):
        print("*"*10)
        print("1 - Cadastrar conta")
        print("2 - Alterar cadastro")
        print("3 - Excluir cadastro")
        print("4 - Listar contas")
        print("0 - Retornar")
        opcao = self.verifica_opcao("ESCOLHA UMA OPÇÃO: ", [1,2,3,4,0])
        return opcao  
    
    
    def mostrar_conta(self, dados_conta):
        print("-"*10)
        for i in dados_conta:
            for k,v in i.items():
                print(k, ": ", v)
            print("-"*10)

    def pegar_dados_conta(self):
        dados_conta = []
        dados_conta.append(int(input("Digite o numero da conta: ")))
        dados_conta.append(input("Digite o tipo da conta: "))
        dados_conta.append(input("Digite o nome do cliente: "))
        dados_conta.append(input("Digite o nome do funcionario: "))
        return dados_conta
        
    
    def buscar_conta(self):
        return int(input(("Digite o número da conta: ")))
        
    def mostrar_mensagem(self,mensagens):
        return super().mostrar_mensagem(mensagens)
    
    
    
from limite.tela import Tela


class TelaSistema(Tela):
    
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def tela_opcoes(self):
        print("*"*10)
        print("1 - Cliente")
        print("2 - Funcionário")
        print("3 - Conta")
        print("4 - Operações")
        print("0 - Encerrar")
        opcao = self.verifica_opcao("ESCOLHA UMA OPÇÃO: ", [1,2,3,4,0])
        return opcao
    
    def mostrar_mensagem(self,mensagens):
        return super().mostrar_mensagem(mensagens)

from excecoes.valor_invalido_exception import ValorInvalidoException
from tela import Tela


class TelaConta(Tela):
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def tela_opcoes(self):
        print("*"*10)
        print("1 - Cadastrar cliente")
        print("2 - Alterar cadastro")
        print("3 - Excluir cadastro")
        print("4 - Listar clientes")
        print("0 - Retornar")
        opcao = self.verifica_opcao("ESCOLHA UMA OPÇÃO: ", [1,2,3,4,0])
        return opcao  
    
    
    def mostrar_conta(self, dados_conta):
        for i in dados_conta:
            for k,v in i:
                print(k, ": ", v)
            print("-"*10)

    def pegar_dados_conta():
        pass
    
    def buscar_conta():
        return int(input(("Digite o número da conta: ")))
        
    def mostrar_mensagem(mensagens):
        return super().mostrar_mensagem(mensagens)
    
    
    
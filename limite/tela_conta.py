from enums.tipo_conta import TipoConta
from limite.tela import Tela


class TelaConta(Tela):
    def verifica_opcao(self, mensagem, inteiros_validos):
        return super().verifica_opcao(mensagem, inteiros_validos)
    
    def tela_opcoes(self):
        print("1 - Cadastrar conta")
        print("2 - Alterar cadastro")
        print("3 - Excluir cadastro")
        print("4 - Listar contas")
        print("0 - Retornar")
        opcao = self.verifica_opcao("Escolhe uma opção: ", [1,2,3,4,0])
        return opcao  
    
    
    def mostrar_conta(self, dados_conta):
        print("-"*10)
        for i in dados_conta:
            print(f"Número: {i.numero}")
            print(f"Tipo: {i.tipo.name.capitalize()}")
            print(f"Cliente: {i.cliente.capitalize()}")
            print(f"Funcionário: {i.funcionario.capitalize()}")
            print(f"Saldo: {i.saldo :.2f}")
            print("-"*10)

    def pegar_dados_conta(self):
        dados_conta = {}
        dados_conta["numero"] = (int(input("Digite o numero da conta: ")))
        tipo = input("Digite o tipo da conta: ")
        if (not getattr(TipoConta, tipo)):
            raise AttributeError
        dados_conta["tipo"] = (getattr(TipoConta, tipo))
        dados_conta["cliente"] = (input("Digite o cpf do cliente: "))
        dados_conta["funcionario"] = (input("Digite o cpf do funcionario: "))
        return dados_conta
        
    
    def buscar_conta(self):
        return int(input(("Digite o número da conta: ")))
        
    def mostrar_mensagem(self,mensagem):
        return super().mostrar_mensagem(mensagem)
    
    
    
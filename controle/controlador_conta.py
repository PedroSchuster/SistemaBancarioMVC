from excecoes.valor_invalido_exception import ValorInvalidoException
from excecoes.cadastro_exception import CadastroException
from entidade.conta import Conta
from limite.tela_conta import TelaConta


class ControladorConta:
    
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__tela_conta = TelaConta()
        self.__contas = []
        
    
    def incluir_conta(self):
        dados_conta = self.__tela_conta.pegar_dados_conta()
        conta = Conta(dados_conta[0],dados_conta[1],
                      dados_conta[2],dados_conta[3])
        
        if (self.pegar_contar_por_numero(conta.numero)):
           raise CadastroException("Cadastro duplicado!")
        
        if (isinstance(conta,Conta) ):
            self.__contas.append(conta)
        
    
    def alterar_conta(self):
        numero_conta = self.__tela_conta.buscar_conta()
        conta = self.pegar_contar_por_numero(numero_conta)
        if (conta == None):
            raise CadastroException("Conta não encontrada")      
        
        self.__tela_conta.mostrar_mensagem(["Novos dados da conta: "])
        dados_conta = self.__tela_conta.pegar_dados_conta()
        self.__contas[self.__contas.index(conta)] = Conta(dados_conta[0],dados_conta[1],
        dados_conta[2],dados_conta[3])
        return self.__tela_conta.mostrar_mensagem(["Conta alterada com sucesso!"])
    
    def excluir_conta(self):
        numero_conta = self.__tela_conta.buscar_conta()
        conta = self.pegar_contar_por_numero(numero_conta)
        if (conta == None):
            raise CadastroException("Conta não encontrada")   
        self.__contas.pop(self.__contas.index(conta))
        return self.__tela_conta.mostrar_mensagem(["Conta excluida com sucesso!"])
                
    
    def listar_contas(self):
        lista = []
        if (self.__contas):
            for i in self.__contas:
                lista.append({"Cliente" : i.cliente, "Numero da conta" : str(i.numero),"Saldo":i.saldo})
        else:
            raise CadastroException("Nenhuma conta cadastrada")      

            
        self.__tela_conta.mostrar_mensagem(["Lista das contas: "])
        return self.__tela_conta.mostrar_conta(lista)
    
    def pegar_contar_por_numero(self, numero):
        if self.__contas:
            for i in self.__contas:
                if i.numero == numero:
                    return i
        return None
        
    
    def registrar_operacao(self,conta, operacao):
        conta.operacoes.append(operacao)
        
    def abre_tela(self):
        opcoes = {1: self.incluir_conta, 2:self.alterar_conta, 3: self.excluir_conta, 4: self.listar_contas}
        while True:
            try:
                opcao = self.__tela_conta.tela_opcoes()
                
                if opcao == 0:
                    break

                opcoes[opcao]() 
           
            except ValueError:
                self.__tela_conta.mostrar_mensagem(["Valor inválido, digite um número inteiro"])
            except ValorInvalidoException as e:
                self.__tela_conta.mostrar_mensagem([e.mensagem])
            except CadastroException as e:
                self.__tela_conta.mostrar_mensagem([e.mensagem])  

    
    
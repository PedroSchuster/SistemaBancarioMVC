import threading
import time
from enums.tipo_conta import TipoConta
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
        
        conta = Conta(dados_conta["numero"], dados_conta["tipo"],
                      dados_conta["cliente"],dados_conta["funcionario"])
        
        if (self.pegar_contar_por_numero(conta.numero)):
           raise CadastroException("Cadastro duplicado!")
        
        if (isinstance(conta,Conta) ):
            self.__contas.append(conta)
        
        if (conta.tipo == TipoConta.poupanca):
            threading.Thread(target=self.calculo_poupanca, args=(conta,), daemon=True).start()
        
    
    def alterar_conta(self):
        numero_conta = self.__tela_conta.buscar_conta()
        conta = self.pegar_contar_por_numero(numero_conta)
        if (not conta):
            raise CadastroException("Conta não encontrada")      
        
        self.__tela_conta.mostrar_mensagem("Novos dados da conta: ")
        dados_conta = self.__tela_conta.pegar_dados_conta()
        conta.numero = dados_conta["numero"]
        conta.tipo = dados_conta["tipo"]
        conta.cliente = dados_conta["cliente"]
        conta.funcionario = dados_conta["funcionario"]

        if (conta.tipo == TipoConta.poupanca):
            threading.Thread(target=self.calculo_poupanca, args=(conta,), daemon=True).start()
            
        return self.__tela_conta.mostrar_mensagem("Conta alterada com sucesso!")
    
    def excluir_conta(self):
        numero_conta = self.__tela_conta.buscar_conta()
        conta = self.pegar_contar_por_numero(numero_conta)
        if (conta == None):
            raise CadastroException("Conta não encontrada")   
        self.__contas.remove(conta)
        return self.__tela_conta.mostrar_mensagem("Conta excluida com sucesso!")
                
    
    def listar_contas(self):
        if (self.__contas):
            self.__tela_conta.mostrar_mensagem("Lista das contas: ")
            return self.__tela_conta.mostrar_conta(self.__contas)
        else:
            raise CadastroException("Nenhuma conta cadastrada")      

    
    def pegar_contar_por_numero(self, numero):
        if self.__contas:
            for i in self.__contas:
                if i.numero == numero:
                    return i
        return None
        
    def calculo_poupanca(self, conta):
        while True:
            conta.saldo *= 1.005
            time.sleep(5)

    def abre_tela(self):
        opcoes = {1: self.incluir_conta, 2:self.alterar_conta, 3: self.excluir_conta, 4: self.listar_contas}
        while True:
            try:
                opcao = self.__tela_conta.tela_opcoes()
                
                if opcao == 0:
                    break

                opcoes[opcao]() 
           
            except ValueError:
                self.__tela_conta.mostrar_mensagem("Valor inválido, verifique se o tipo do valor da entrada está correto!")
            except AttributeError:
                self.__tela_conta.mostrar_mensagem("Tipo de conta não encontrado!")
            except ValorInvalidoException as e:
                self.__tela_conta.mostrar_mensagem(e.mensagem)
            except CadastroException as e:
                self.__tela_conta.mostrar_mensagem(e.mensagem)  
            

    
    
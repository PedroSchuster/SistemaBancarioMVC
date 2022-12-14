import threading
import time
from enums.tipo_conta import TipoConta
from excecoes.valor_invalido_exception import ValorInvalidoException
from excecoes.cadastro_exception import CadastroException
from entidade.conta import Conta
from limite.tela_conta import TelaConta
from dao.dao_main import DAO

class ControladorConta:
    
    def __init__(self, controlador_sistema) -> None:
        self.__controlador_sistema = controlador_sistema
        self.__contas = []
        self.__tela_conta = TelaConta()
        self.__dao = controlador_sistema.dao

    def incluir_conta(self):
        dados_conta = self.__tela_conta.pegar_dados_conta()
        
        if (not dados_conta):
            return

        if (not dados_conta["cliente"] or not dados_conta["funcionario"]
            or not dados_conta["tipo"] or not dados_conta["numero"]):
            raise CadastroException("Há campos para serem preenchidos!")

        index_cliente =  self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(dados_conta["cliente"])
        cliente = self.__dao.get_one(index_cliente, 'clientes') 
        
        if (not cliente):
            raise CadastroException("Cliente não encontrado")
        
        funcionario = self.__dao.get_one(self.__controlador_sistema.controlador_funcionario.pega_funcionario_por_cpf(dados_conta["funcionario"]), 'funcionarios')
        
        if (not funcionario):
            raise CadastroException("Funcionário não encontrado")
        
        if (self.pegar_contar_por_numero(int(dados_conta["numero"])) is not None):
           raise CadastroException("Cadastro duplicado!")

        conta = Conta(int(dados_conta["numero"]), TipoConta[dados_conta["tipo"]],
                      cliente, funcionario)

        if ((len(cliente.contas) > 0 and len(cliente.contas) < 2 and cliente.contas[0].tipo != conta.tipo)
            or len(cliente.contas) == 0):
            if (isinstance(conta,Conta)):
                self.__dao.add('contas', conta)
                cliente.add_conta(conta)
                self.__dao.modify(index_cliente, 'clientes', cliente)
                
        else:
            raise CadastroException("Não foi possível registrar essa conta ao cliente cadastrado")

        if (conta.tipo == TipoConta.poupanca):
            threading.Thread(target=self.calculo_poupanca, args=(conta,), daemon=True).start()
        

        
        return self.__tela_conta.mostrar_mensagem("Conta registrada com sucesso!")
    
    def alterar_conta(self):
        index = self.listar_contas()

        if (index == None):
            return    
        
        self.__tela_conta.mostrar_mensagem("Novos dados da conta: ")
        dados_conta = self.__tela_conta.pegar_dados_conta()
        
        cliente = self.__dao.get_one( self.__controlador_sistema.controlador_cliente.pega_cliente_por_cpf(dados_conta["cliente"]), 'clientes')

        if (not cliente):
            raise CadastroException("Cliente não encontrado")
        
        funcionario = self.__dao.get_one(self.__controlador_sistema.controlador_funcionario.pega_funcionario_por_cpf(dados_conta["funcionario"]), 'funcionarios')

        if (not funcionario):
            raise CadastroException("Funcionario não encontrado")
        
        conta = Conta(int(dados_conta["numero"]), TipoConta[dados_conta["tipo"]], cliente, funcionario)

        if (isinstance(conta, Conta)):
            self.__dao.modify(index, 'contas', conta)
        else:
            raise Exception

        if (conta.tipo == TipoConta.poupanca):
            threading.Thread(target=self.calculo_poupanca, args=(conta,), daemon=True).start()
            
        return self.__tela_conta.mostrar_mensagem("Conta alterada com sucesso!")
    
    def excluir_conta(self):
        index = self.listar_contas()
        if (index == None):
            return 

        conta = self.__dao.get_one(index, 'contas')
        cliente = conta.cliente
        lista_clientes = self.__dao.get_list('clientes')
        index_cliente = lista_clientes.index(cliente)
        cliente.remove_conta(conta)

        self.__dao.modify(index_cliente, 'clientes', cliente)
        self.__dao.remove(index, 'contas')
        return self.__tela_conta.mostrar_mensagem("Conta excluida com sucesso!")
                
    def listar_contas(self):
        self.__contas = self.__dao.get_list('contas')
        lista_numeros = []
        for i in self.__contas:
            lista_numeros.append(i.numero)
        if (self.__contas):
            return self.pegar_contar_por_numero(self.__tela_conta.listar_contas(lista_numeros))
        else:
            raise CadastroException("Nenhuma conta cadastrada")      

    
    def mostrar_conta(self):
        index = self.listar_contas()
        if (index == None):
            return
        return self.__tela_conta.mostrar_conta(self.__contas[index])
        

    def pegar_contar_por_numero(self, numero):
        if (numero):
            self.__contas = self.__dao.get_list('contas')
            if self.__contas:
                for i in range(len(self.__contas)) :
                    if self.__contas[i].numero == numero:
                        return i
        return None
        
    def calculo_poupanca(self,conta):
        index = self.__contas.index(conta)
        while True:
            conta.saldo *= 1.005
            self.__dao.modify(index,'contas',conta)
            time.sleep(5)

    def abre_tela(self):
        opcoes = {1: self.incluir_conta, 2:self.alterar_conta, 3: self.excluir_conta, 4: self.mostrar_conta}
        while True:
            try:
                opcao = self.__tela_conta.tela_opcoes()
                
                if opcao == 0:
                    break

                opcoes[opcao]() 
            
            except ValorInvalidoException as e:
                self.__tela_conta.mostrar_mensagem(e.mensagem)
            except CadastroException as e:
                self.__tela_conta.mostrar_mensagem(e.mensagem)  
            except AttributeError:
                self.__tela_conta.mostrar_mensagem("Escolhe um tipo de conta correto")  
            except Exception:
                self.__tela_conta.mostrar_mensagem("Ocorreu um erro inesperado!")  

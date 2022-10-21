from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente

class ControladorCliente:

    def __init__(self, controlador_sistema):
        self.__cliente = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()

    def pega_cliente_por_cpf(self, cpf: int):
        for cliente in self.__cliente:
            if cliente.cpf == cpf:
                return cliente
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], dados_cliente["telefone"],
                        dados_cliente["idade"])
        self.__cliente.append(cliente)

    def alterar_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        Cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if Cliente is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            Cliente.nome = novos_dados_cliente["nome"]
            Cliente.telefone = novos_dados_cliente["telefone"]
            Cliente.cpf = novos_dados_cliente["cpf"]
            Cliente.idade = novos_dados_cliente["idade"]
            self.lista_clientes()
        else:
            self.__tela_cliente.mostra_mensagem("cliente nã existente")
    
    def exluir_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega._cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            self.__cliente.remove(cliente)
            self.lista_clients()
        else:
            self.__tela_cliente.mosta_mensagem(" cliente não existente ")
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.alterar_cliente, 3: self.lista_cliente,
                        4: self.excluir_cliente,
                        0: self.retornar}
                
        continua = True
        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
from entidade.endereco import Endereco
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
        
        dados_endereco = self.__tela_cliente.pegar_dados_endereco
        
        self.add_endereco(cliente, dados_endereco["rua"], dados_endereco["complemento"], dados_endereco["complemento"], 
        dados_endereco["cidade"], dados_endereco["cep"])
        
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
            self.__tela_cliente.mostra_mensagem("cliente não existente")

    def lista_cliente(self):
        for cliente in self.__cliente:
            self.__tela_cliente.mostra_cliente(
                {"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf, "idade": cliente.idade, "contas" : cliente.contas})
    
    def excluir_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            self.__cliente.remove(cliente)
            self.lista_clients()
        else:
            self.__tela_cliente.mostra_mensagem(" cliente não existente ")
    
    def add_endereco(self, cliente, rua, complemento, bairro, cidade, cep):
        novo_endereco = Endereco( rua,complemento, bairro, cidade, cep)
        cliente.enderecos.append(novo_endereco)

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.excluir_cliente, 3: self.lista_cliente,
                        4: self.alterar_cliente,
                        0: self.retornar}
                
        continua = True

        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()
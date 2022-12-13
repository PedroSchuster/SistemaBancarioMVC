from entidade.endereco import Endereco
from limite.tela_cliente import TelaCliente
from entidade.cliente import Cliente


class ControladorCliente:

    def __init__(self, controlador_sistema):
        self.__cliente = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_cliente = TelaCliente()
        self.__dao = controlador_sistema.dao


    def pega_cliente_por_cpf(self, cpf):
        self.__cliente = self.__dao.get_list('clientes')
        for i in range(len(self.__cliente)):
            if self.__cliente[i].cpf == cpf:
                return i
        return None

    def incluir_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome"], dados_cliente["cpf"], int(dados_cliente["telefone"]),
                          int(dados_cliente["idade"]))

        dados_endereco = self.__tela_cliente.pegar_dados_endereco()

        cliente.add_endereco(dados_endereco["rua"], dados_endereco["bairro"], dados_endereco["complemento"],
                          dados_endereco["cidade"], dados_endereco["cep"])

        self.__dao.add('clientes', cliente)

    def alterar_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        index = self.pega_cliente_por_cpf(cpf_cliente)

        if index is not None:
            novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()
            cliente = Cliente(novos_dados_cliente["nome"], novos_dados_cliente["cpf"], int(novos_dados_cliente["telefone"]), int(novos_dados_cliente["idade"]))
            self.__dao.modify(index, 'clientes', cliente)
            self.lista_cliente()
        else:
            self.__tela_cliente.mostra_mensagem("cliente não existente")

    def lista_cliente(self):
        self.__cliente = self.__dao.get_list('clientes')
        for cliente in self.__cliente:
            self.__tela_cliente.mostra_cliente(
                {"nome": cliente.nome, "telefone": cliente.telefone, "cpf": cliente.cpf, "idade": cliente.idade})

    def excluir_cliente(self):
        self.lista_cliente()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        index = self.pega_cliente_por_cpf(cpf_cliente)

        if index is not None:
            self.__dao.remove(index,'clientes')
            self.lista_cliente()
        else:
            self.__tela_cliente.mostra_mensagem(" cliente não existente ")

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente, 2: self.excluir_cliente, 3: self.lista_cliente,
                        4: self.alterar_cliente,
                        0: self.retornar}

        continua = True

        while continua:
            lista_opcoes[self.__tela_cliente.tela_opcoes()]()

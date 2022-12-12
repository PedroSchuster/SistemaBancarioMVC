from logging import raiseExceptions
from entidade.endereco import Endereco
from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int, idade: int):
        if not isinstance(nome, str):
            raise Exception(" Nome inválido! Digite apenas letras! ")
        if not isinstance(cpf, str):
            raise Exception(" Cpf inválido! Digite apenas números! ")
        if not isinstance(telefone, int):
            raise Exception(" Telefone inválido! Digite apenas números! ")
        if not isinstance(idade, int):
            raise Exception(" Idade inválida! Digite apenas números! ")

        super().__init__(nome, cpf, telefone)
        if isinstance(idade, int):
            self.__idade = idade

        self.__contas = []
        self.__enderecos = []

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else: 
            raise Exception(" Entre com um valor positivo! ")
    

    def add_conta(self, conta):
        self.__contas.append(conta)

    def add_endereco(self, rua, complemento, bairro, cidade, cep):
        novo_endereco = Endereco(rua, complemento, bairro, cidade, cep)
        self.__enderecos.append(novo_endereco)
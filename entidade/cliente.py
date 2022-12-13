from logging import raiseExceptions
from entidade.endereco import Endereco
from entidade.pessoa import Pessoa


class Cliente():
    def __init__(self, nome: str, cpf: str, telefone: int, idade: int):
        if not isinstance(nome, str):
            raise Exception(" Nome inválido! Digite apenas letras! ")
        if not isinstance(telefone, int):
            raise Exception(" Telefone inválido! Digite apenas números! ")
        if not isinstance(idade, int):
            raise Exception(" Idade inválida! Digite apenas números! ")

        if isinstance(idade, int):
            self.__idade = idade
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__contas = []
        self.__enderecos = []

    @property
    def idade(self) -> int:
        return self.__idade

    @property 
    def contas(self):
        return self.__contas

    @property
    def enderecos(self):
        return self.__enderecos

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def cpf(self) -> int:
        return self.__cpf

    @property
    def telefone(self) -> int:
        return self.__telefone

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf 

    @telefone.setter
    def telefone(self, telefone: int):
        if isinstance(telefone, int):
            self.__telefone = telefone

    @idade.setter
    def idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else: 
            raise Exception(" Entre com um valor positivo! ")
    
    def add_conta(self, conta):
        self.__contas.append(conta)

    def remove_conta(self, conta):
        self.__contas.remove(conta)

    def add_endereco(self, rua, complemento, bairro, cidade, cep):
        novo_endereco = Endereco(rua, complemento, bairro, cidade, cep)
        self.__enderecos.append(novo_endereco)
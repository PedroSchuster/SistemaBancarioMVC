from logging import raiseExceptions
from entidade.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, telefone: int, idade: int):
        if not isinstance(nome, str):
            raise Exception(" Nome inválido! Digite apenas letras! ")
        if not isinstance(cpf, int):
            raise Exception(" Cpf inválido! Digite apenas números! ")
        if not isinstance(telefone, int):
            raise Exception(" Telefone inválido! Digite apenas números! ")
        if not isinstance(idade, int):
            raise Exception(" Idade inválida! Digite apenas números! ")

        super().__init__(nome, cpf, telefone)
        if isinstance(idade, int):
            self.__idade = idade

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade > 0:
            self.__idade = idade
        else: 
            raise Exception(" Entre com um valor positivo! ")

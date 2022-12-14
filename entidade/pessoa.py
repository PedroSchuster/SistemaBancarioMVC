from abc import ABC, abstractclassmethod


class Pessoa(ABC):

    @abstractclassmethod
    def __init__(self, nome: str, cpf: str, telefone: int):
        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(cpf, str):
            self.__cpf = cpf

        if isinstance(telefone, int):
            self.__telefone = telefone

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
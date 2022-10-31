class Endereco:

    def __init__(self, rua : str, complemento : str, bairro : str, cidade : str, cep : str):
        self.__rua = rua
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep


    @property
    def rua(self):
        return self.__rua
    
    @rua.setter
    def rua(self, rua):
        self.__rua = rua
    
    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    @property 
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro
    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, cep):
        self.__cep = cep
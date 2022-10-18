class ValorInvalidoException(Exception):
    def __init__(self, valor_inserido):
        self.mensagem = f"O valor {valor_inserido} não é válido"
        super().__init__(self.mensagem)
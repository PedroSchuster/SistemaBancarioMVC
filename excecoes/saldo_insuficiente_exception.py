class SaldoInsuficienteException(Exception):
    def __init__(self, num_conta):
        self.mensagem = f"A conta {num_conta} não tem saldo suficiente!"
        super().__init__(self.mensagem)
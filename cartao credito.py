from cartao import Cartao


class Cartao_Credito(Cartao):
    def __init__(self, conta_vinculada, cliente, numero):
        super().__init__(conta_vinculada, cliente, numero)
        self.tipo = 'Crédito'
        self.fatura = 0

    def debito(self, valor):
        self.fatura += valor

    def pagar_fatura(self):
        self.conta_vinculada.debito(self.fatura)
        self.fatura = 0

    def get_fatura(self):
        return self.fatura

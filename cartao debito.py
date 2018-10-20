from cartao import Cartao


class Carta_Debito(Cartao):
    def __init__(self,conta_vinculada, cliente, numero):
        self.tipo = 'Débito'
        super().__init__(conta_vinculada, cliente, numero)

    def debito(self, valor):
        return self.conta_vinculada.debito(valor)

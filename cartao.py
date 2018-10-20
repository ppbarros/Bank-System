class Cartao:
    def __init__(self, conta_vinculada, cliente, numero):
        self.conta_vinculada = conta_vinculada
        self.cliente = cliente
        self.numero = numero

    def get_conta(self):
        return self.conta_vinculada

    def get_cliente(self):
        return self.cliente

    def get_numero(self):
        return self.numero

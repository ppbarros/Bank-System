class Conta:
    def __init__(self, ag, conta, tipo, cliente):
        self.ag = ag
        self.conta = conta
        self.tipo = tipo
        self.saldo = 0
        self.cliente = cliente

    def get_saldo(self):
        return self.saldo

    def get_ag(self):
        return self.ag

    def get_conta(self):
        return self.conta

    def deposito(self, valor):
        self.saldo += valor
        return True

    def debito(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False

    def transferencia(self, valor, conta_destino):
        if self.saldo >= valor:
            conta_destino.deposito(valor)
            return True
        else:
            return False

    def __str__(self):
        return f'''Agência: {self.ag}
Número Conta: {self.conta}
Tipo: {self.tipo}'''

from cliente import Cliente


class P_Juridica(Cliente):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self.cnpj = cnpj

    def get_cnpj(self):
        return self.cnpj

    def __str__(self):
        return f''''{super().__str__()}
CNPJ: {self.cnpj}'''

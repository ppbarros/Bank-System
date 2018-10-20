class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco

    def __str__(self):
        return f'''Nome: {self.nome}
Endereço: {self.endereco}'''

from cliente import Cliente


class P_Fisica(Cliente):
    def __init__(self, nome, endereco, cpf, idade, sexo):
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.idade = idade
        self.sexo = sexo

    def get_cpf(self):
        return self.cpf

    def get_idade(self):
        return self.idade

    def get_sexo(self):
        return self.sexo

    def __str__(self):
        return f'''{super().__str__()}
CPF: {self.cpf}
Idade: {self.idade}
Sexo: {self.sexo}'''

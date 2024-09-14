class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome 
        self.salario_base = salario_base

        def valores(self):
            ...
class Gerente(Empregado):
    def valores(self):
        return f'{self.nome} recebe {self.salario_base}'

class Vendedor(Empregado):
    def valores(self):
        return f'{self.nome} recebe {self.salario_base + (self.salario_base*0.02)}'
    


''
gerente1 = Gerente("Luis", 2000)
print(gerente1.valores())
vendedor1 = Vendedor("vitor", 1400)
print(vendedor1.valores())

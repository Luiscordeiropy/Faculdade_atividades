class Animal:
    def __init__(self, nome):
        self.nome = nome

        def falar(self):
            ...
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} emite latido!"

class Gato(Animal):
    def falar(self):
        return f"{self.nome} emite miado!"

melissa = Cachorro("Melissa")
floquinho = Gato("Floquinho")

print(melissa.falar())
print(floquinho.falar())
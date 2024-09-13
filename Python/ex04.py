# Crie uma classe Aluno que encapsule os dados de um aluno, como nome e notas, e forneça métodos para manipular essas informações.​Requisitos:​Crie a classe Aluno com atributos privados __nome, __nota1 e __nota2.​Implemente métodos públicos para definir e acessar as notas e o nome.​

class Aluno:
    def __init__(self, nome: str, nota1:float, nota2:float ):
        self.__nome = nome
        self.__nota1 = nota1
        self.__nota2 = nota2

    def dizer_nome(self):
        print(f"Nome: {self.__nome}")

    def dizer_nota1(self):
        print(f"nota1: {self.__nota1}")

    def dizer_nota2(self):
        print(f"Nota2: {self.__nota2}")
    
    def dizer_media(self):
        media = self.
        print (media)

aluno = Aluno(nome="Luis", nota1 ="5", nota2 ="7")
aluno.dizer_nome()
aluno.dizer_nota1()
aluno.dizer_nota2()
aluno.dizer_media()

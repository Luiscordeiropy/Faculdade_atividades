class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float ):
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
        print((self.__nota1 + self.__nota2)/2)

aluno = Aluno(nome="Luis", nota1 =5, nota2 =7)

aluno.dizer_nome()
aluno.dizer_nota1()
aluno.dizer_nota2()
aluno.dizer_media()

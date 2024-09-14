class Aluno:
    def __init__(self, nome, nota1, nota2 ):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def dizer_nome(self, ):
        print(self.nome)

    def dizer_nota1(self):
        print(self.nota1)

    def dizer_nota2(self):
        print(self.nota2)

    def dizer_media(self):
        print((self.nota1 + self.nota2)/2)

aluno = Aluno(nome="Luis", nota1 =5, nota2 =7)

aluno.dizer_nome()
aluno.dizer_nota1()
aluno.dizer_nota2()
aluno.dizer_media()

aluno = Aluno(nome="pdedr", nota1 =5, nota2 =7)
aluno.dizer_nome()

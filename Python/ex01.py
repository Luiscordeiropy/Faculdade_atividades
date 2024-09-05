#Receber 4 notas pelo usuário e no final calcular a média final, se for maior ou igual a 7, aprovado se não reprovado
soma_nota = 0
for c in range(4):
    nota = float(input("Digite sua nota: "))
    soma_nota += nota
media = soma_nota/4
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
#Receber a quantidade de notas pelo usuário que será calculado e no final calcular a média final
soma_nota = cont = 0

while True:
    nota = float(input("Digite sua nota (digite 000 para encerrar): "))
    if nota == 000:
        break
    soma_nota += nota
    cont += 1

media = soma_nota/cont
print(f"A sua média é {media}")
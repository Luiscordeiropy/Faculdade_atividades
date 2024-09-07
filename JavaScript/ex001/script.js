let soma_nota = 0
let nota = 0

for (i=1; i<5; i++){
    nota = parseInt(prompt("Informe a sua idade: "))
    soma_nota += nota
}
soma_nota = soma_nota/4
alert(soma_nota)
let num01 = parseInt(prompt("Digite o primeiro número: "))
alert("SELECIONE O OPERADOR \n1 -- soma \n2 -- subtração\n3 -- multiplicação\n4 -- divisão") 
let operador = prompt("Digite o operador que você quer utilizar: ")
let num02 = parseInt(prompt("Digite o segundo número: "))

if (operador == 1) {
    alert(num01 + num02)
}
else if (operador == 2) {
    alert(num01 - num02)
}
else if (operador == 3) {
    alert(num01 * num02)
}
else if(operador == 4) {
    alert(num01 / num)
}
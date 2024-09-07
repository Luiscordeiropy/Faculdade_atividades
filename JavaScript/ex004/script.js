let num = parseInt(prompt("Digite um número: "));

const interval = setInterval(() => {
    if (num > 0) {
        document.getElementById("countdown").innerHTML = num;
        num--;
    } else {
        clearInterval(interval);
        document.getElementById("countdown").innerHTML = 'Contagem encerrada!';
    }
}, 1000);

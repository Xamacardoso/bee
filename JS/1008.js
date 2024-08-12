var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function main(){
    const num = parseInt(lines.shift());
    const horas = parseInt(lines.shift());
    const valor = parseFloat(lines.shift());
    
    console.log(`NUMBER = ${num}`);
    console.log(`SALARY = U$ ${(horas*valor).toFixed(2)}`);
}

main();
import {getnumber} from './io_utils.js';
function main() {
    let valor = parseFloat(getnumber());
    let notas100 = Math.floor(valor / 100)
    valor = valor % 100
    let notas50 = Math.floor(valor / 50)
    valor = valor % 50
    let notas20 = Math.floor(valor / 20)
    valor = valor % 20
    let notas10 = Math.floor(valor / 10)
    valor = valor % 10
    let notas5 = Math.floor(valor / 5)
    valor = valor % 5
    let notas2 = Math.floor(valor / 2)
    valor = valor % 2
    let moedas1 = Math.floor(valor/1)
    valor = valor - moedas1
    let moedas50 = Math.floor(valor /0.5)
    valor = valor - moedas50 / 2
    let moedas25 = Math.floor(valor /0.25)
    valor = valor - moedas25 / 4
    let moedas10 = Math.floor(valor / 0.1)
    valor = valor - moedas10 / 10
    let moedas5 = Math.floor(valor / 0.05)
    valor = valor - moedas5 / 20
    let moedas1c = Math.floor(valor / 0.009)
    console.log(`NOTAS:
${notas100} nota(s) de R$ 100,00
${notas50} nota(s) de R$ 50,00
${notas20} nota(s) de R$ 20,00
${notas10} nota(s) de R$ 10,00
${notas5} nota(s) de R$ 5,00
${notas2} nota(s) de R$ 2,00
MOEDAS:
${moedas1} moeda(s) de R$ 1.00
${moedas50} moeda(s) de R$ 0.50
${moedas25} moeda(s) de R$ 0.25
${moedas10} moeda(s) de R$ 0.10
${moedas5} moeda(s) de R$ 0.05
${moedas1c} moeda(s) de R$ 0.01`)
}

main()

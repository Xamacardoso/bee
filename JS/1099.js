import { getnumber } from "./io_utils.js"

function main(){
    const n = getnumber()
    let count = 1
    let soma
    
    while(count<=n){
        soma = 0
        let [x, y] = getnumber().split(' ').map(Number)
        soma = impares(x,y)
        console.log(soma)
        
        count++
    }
    
}

main()

function impares(x,y){
    const maior = x>y ? x : y
    let menor = x>y ? y+1 : x+1
    let soma = 0
    while(menor<maior){
        soma += menor % 2 !== 0 ? menor : 0
        menor++
    }
    
    return soma
}
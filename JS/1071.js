import { getnumber } from "./io_utils.js";

function main(){
    const x = getnumber()
    const y = getnumber()
    let soma = 0

    if (x>y){
        let count = y+1
        while (count<x){
            if (count%2!==0){
                soma = soma + count
            }
            count++
        }
    }else if (x<y){
        let count = x+1
        while (count<y){
            if (count%2!==0){
                soma = soma + count
            }
            count++
        }
    }

    console.log(soma)
}

main()
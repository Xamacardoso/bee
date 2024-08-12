import { getnumber } from "./io_utils.js"

function main(){
    const n = getnumber()
    let count = 0
    while(count<n){
        let num = getnumber()
        if (num === 0){
            console.log('NULL')
        }else if (num>0){
            if (num%2===0){
                console.log('EVEN POSITIVE')
            }else{
                console.log('ODD POSITIVE')
            }
        }else if (num<0){
            if (num%2===0){
                console.log('EVEN NEGATIVE')
            }else{
                console.log('ODD NEGATIVE')
            }
        }
        count++
    }
    
}
main()
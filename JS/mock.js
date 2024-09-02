function main(){
    const lala = '1 2 3 4'
    let [a,b,c,d] = lala.split(' ').map(x => parseInt(x))
    
    console.log(typeof(a))
    console.log(a)
    console.log(c)
    console.log(d)
}
main()
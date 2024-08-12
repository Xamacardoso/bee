def main():
    positivos = 0
    soma = 0
    for i in range(6):
        num = float(input());
        if num > 0:
            soma += num;
            positivos += 1;
            
    print(positivos, "valores positivos");
    print(round(soma/positivos, 1))
    

main()
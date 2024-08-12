def main():
    idade = 1;
    count = 0;
    soma = 0;
    while idade > 0:
        idade = int(input());
        if idade > 0:
            count += 1;
            soma += idade;

    print(f"{(soma/count):.2f}");


main();
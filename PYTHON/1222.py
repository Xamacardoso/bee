def main():
    while True:
        try:
            numPalavras, linhasPagina, caracLinha = map(int, input().split());
            entrada = input();

        except EOFError:
            break;

main();
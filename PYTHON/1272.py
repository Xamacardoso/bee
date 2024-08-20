def mostrarPalavra(texto):
    texto = " " + texto
    textoFinal = ""
    for index in range(len(texto)):
        if index > 0 and (texto[index-1] == ' ' and texto[index] != ' '):
            textoFinal += texto[index];

    print(textoFinal);


def main():
    casos = int(input());
    for caso in range(casos):
        entrada = input();
        mostrarPalavra(entrada);



main();
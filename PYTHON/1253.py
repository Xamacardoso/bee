def mostrarConvertido(texto, num):
    textoConvertido = "";
    for index in range(len(texto)):
        codigo = ord(texto[index]) - num;
        if codigo < 65:
            codigo += 26;
        
        textoConvertido += chr(codigo);

    print(textoConvertido);


def main():
    casos = int(input());
    for caso in range(casos):
        entradaTexto = input();
        numCasas = int(input());
        mostrarConvertido(entradaTexto, numCasas);
        

main();
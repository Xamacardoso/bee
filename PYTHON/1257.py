def computarValor(texto, aux):
    soma = 0;
    for index in range(len(texto)): # para cada letra
        caractere = texto[index]; # define quem é o caractere
        
        # soma o valor do caractere, a posicao dele e o numero do caso
        soma += (ord(caractere) - 65) + index + aux;
    

    return soma;



def main():
    numTestes = int(input()); # numero de testes

    for teste in range(numTestes): 
        casos = int(input()); # numero de casos em cada teste
        somaCaso = 0; # zera a soma
        for caso in range(casos):
            entrada = input();
            somaCaso += computarValor(entrada, caso);

        print(somaCaso);



main();
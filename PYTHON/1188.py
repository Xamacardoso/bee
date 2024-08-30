def reduzir(agregadora, lista, inicial):
    acumulado = inicial;
    for item in lista:
        acumulado = agregadora(item, acumulado);

    return acumulado;

def inserir_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i].append(float(input()))

def abaixo_metade(matriz, funcao, operacao):
    verdinhos = [];
    eh_diagonal = lambda x, y: x == y or x + y == len(matriz)-1
    for x in range(len(matriz)//2 +1, len(matriz)): # começa a partir da metade
        for y in range(len(matriz) - x, len(matriz)): # descobre qual coluna devo começar a pegar os verdinhos
            if eh_diagonal(x,y): # para quando chegar em outro amarelinho
                break;

            verdinhos.append(matriz[x][y]);

    return reduzir(funcao, verdinhos, 0) if operacao.lower() == 's' else reduzir(funcao,verdinhos,0)/len(verdinhos);


def main():
    operacao = input();
    gerar_matriz = lambda x : [[] for x in range(x)]
    matriz = gerar_matriz(12);
    inserir_elementos(matriz);


    funcao = lambda x,y: x+y
    print(f'{abaixo_metade(matriz, funcao, operacao):.1f}');
    
    

main();

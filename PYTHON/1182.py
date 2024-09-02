def reduzir(agregadora, lista, inicial):
    acc = inicial;
    for item in lista:
        acc = agregadora(acc, item);

    return acc

def coluna2(matriz,coluna, opcao):
    verdinhos = []
    for x in range(len(matriz)): # começo do verdinho
        verdinhos.append(matriz[x][coluna]);

    return reduzir(lambda x,y: x+y, verdinhos, 0) if opcao.lower() == 's' else reduzir(lambda x,y: x+y, verdinhos, 0)/len(verdinhos);     

def inserir_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i].append(float(input()));

    

def main():
    coluna = int(input())
    opcao = input()
    gerar_matriz = lambda x: [[] for i in range(x)]
    matriz = gerar_matriz(12)
    inserir_elementos(matriz);
    print(f'{coluna2(matriz, coluna, opcao):.1f}')

main();
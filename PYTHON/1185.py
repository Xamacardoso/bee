def reduzir(agregadora, lista, inicial):
    acc = inicial;
    for item in lista:
        acc = agregadora(acc, item);

    return acc

def acima_diag_sec(matriz, opcao):
    verdinhos = []
    for y in range(len(matriz)-1): # começo do verdinho
        for x in range(len(matriz)-1 - y):
            verdinhos.append(matriz[y][x]);

    return reduzir(lambda x,y: x+y, verdinhos, 0) if opcao.lower() == 's' else reduzir(lambda x,y: x+y, verdinhos, 0)/len(verdinhos);     

def inserir_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i].append(float(input()));

    

def main():
    opcao = input()
    gerar_matriz = lambda x: [[] for i in range(x)]
    matriz = gerar_matriz(12)
    inserir_elementos(matriz);
    print(f'{acima_diag_sec(matriz, opcao):.1f}')

main();
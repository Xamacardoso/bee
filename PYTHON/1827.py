def main():
    while True:
        try:
            n = int(input());
            matriz = [[0 for j in range(n)] for i in range(n)];
            for i in range(len(matriz)):
                for j in range(len(matriz)):
                    if i == j:
                        matriz[i][j] = 2;
                    if i + j == len(matriz) -1: 
                        matriz[i][j] = 3;
            
            aux = len(matriz)//3
            for i in range(aux, len(matriz) - aux):
                for j in range(aux, len(matriz) - aux):
                    matriz[i][j] = 1;

            meio = len(matriz)//2
            matriz[meio][meio] = 4

            for linha in matriz:
                print(*linha,sep='')
            print()
        except EOFError:
            break

main();
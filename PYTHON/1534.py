def gerar_matriz123(n):
    matriz = [[3 for i in range(n)] for j in range(n)]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                matriz[i][j] = 1
                
            if i + j == len(matriz) - 1:
                matriz[i][j] = 2
            

    return matriz

def main():
    while True:
        try:
            n = int(input())
            for linha in gerar_matriz123(n):
                print(*linha, sep='')
                
        

        except EOFError:
            break
        
    
main();
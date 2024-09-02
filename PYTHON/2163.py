def has_sevens_near(matriz, x, y):
    if (x > len(matriz) - 2 or x == 0) or (y > len(matriz[0]) - 2 or y == 0):
        return False
    # mapeia todas as casas próximas menos a casa que possui x e y como coordenada, a casa do 42

    return True if (matriz[x-1][y-1] == 7 and matriz[x][y-1] == 7 and matriz[x+1][y-1] == 7 and\
    matriz[x-1][y] == 7 and matriz[x+1][y] == 7 and \
    matriz[x-1][y+1] == 7 and matriz[x][y+1] == 7 and matriz[x+1][y+1] == 7) else False

def inserir_elementos(matriz, linhas, colunas):
    for i in range(linhas):
        matriz[i] = list(map(int, input().split(' ')));



def main():
    linhas, colunas = map(int, input().split(' ')); # area da varredura
    gerar_matriz = lambda x: [[] for i in range(x)]
    matriz = gerar_matriz(linhas)
    inserir_elementos(matriz, linhas, colunas)
    for linha in range(linhas):
        for coluna in range(colunas):
            if matriz[linha][coluna] == 42:
                if has_sevens_near(matriz, linha, coluna):
                    print(linha+1, coluna+1)
                    return
    
    print("0 0")


main();
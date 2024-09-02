def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        matriz = [[1 for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                if (i < n - i - 1):
                    distancialinha = i;
                else:
                    distancialinha = n - i - 1;
                    
                if (j < n - i - 1):
                    distanciacoluna = j;
                else:
                    distanciacoluna = n - j - 1;
                
                if (distancialinha < distanciacoluna):
                    dist = distancialinha;
                else:
                    dist = distanciacoluna;
                
                matriz[i][j] = dist+1;
                
                
        for linha in matriz:
            print(' ', end= ' ')
            print(*linha, sep= ' ')
            
        print()
    
    
main();
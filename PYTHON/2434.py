def main():
    n, s = map(int, input().split(' '))
    count = 1
    conta = s
    menor = conta
    
    while count<= n:
        movimentacao = int(input())
        conta += movimentacao
        if conta < menor:
            menor = conta
        count += 1
    
    print(menor)
    
main()
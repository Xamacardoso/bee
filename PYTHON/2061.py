def main():
    abas, n_acoes = map(int, input().split(' '))
    count = 1
    while count <= n_acoes:
        acao = str(input())
        if acao == 'fechou':
            abas += 1
        else:
            abas -= 1
        
        count +=1 

    print(abas)

main()
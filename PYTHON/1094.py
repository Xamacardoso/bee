def main():
    n = int(input())
    count = 0
    
    total, ratos, coelhos, sapos = 0, 0, 0, 0

    while count<n:
        qtd, tipo = input().split(' ')
        qtd = int(qtd)
        while qtd<1 or qtd>15:
            qtd, tipo = input().split(' ')
            qtd = int(qtd)
        tipo = str(tipo)
        count+= 1
        if tipo == 'S':
            sapos += qtd
        elif tipo == 'C':
            coelhos += qtd
        elif tipo == 'R':
            ratos +=  qtd
        
        total+=qtd

    pct_ratos = ratos/total*100
    pct_sapos = sapos/total*100
    pct_coelhos = coelhos/total*100

    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {coelhos}')
    print(f'Total de ratos: {ratos}')
    print(f'Total de sapos: {sapos}')
    print(f'Percentual de coelhos: {pct_coelhos:.2f} %')
    print(f'Percentual de ratos: {pct_ratos:.2f} %')
    print(f'Percentual de sapos: {pct_sapos:.2f} %')
            
    
main()
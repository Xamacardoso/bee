def main():
    m, n = map(int, input().split(' '))
    while m>0 and n>0:
        soma = 0
        lista = ''
        if n>m:
            count = m
            while count <=n:
                lista += f'{count} '
                soma += count
                count+= 1
        elif m>n:
            count = n
            while count <=m:
                lista += f'{count} '
                soma += count
                count += 1
        print(f'{lista}Sum={soma}')
        m, n = map(int, input().split(' '))
    
    
main()
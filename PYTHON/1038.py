def main():
    codigo, quantidade = map(int, input().split(' '))
    if codigo == 1:
        preco = quantidade * 4
    if codigo == 2:
        preco = quantidade * 4.50
    if codigo == 3:
        preco = quantidade * 5.00
    if codigo == 4:
        preco = quantidade * 2
    if codigo == 5:
        preco = quantidade * 1.5
    
    print(f'Total: R$ {preco:.2f}')
        
    
main()
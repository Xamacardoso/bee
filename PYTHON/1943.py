def main():
    posicao = int(input())
    if posicao > 50:
        top = '100'
    elif posicao > 25:
        top = '50'
    elif posicao > 10:
        top = '25'
    elif posicao > 5:
        top = '10'
    elif posicao > 3:
        top = '5'
    elif posicao > 1:
        top = '3'
    else:
        top = '1'
    
    print(f'Top {top}')
    
main()
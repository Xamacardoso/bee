def main():
    i = 1
    j = 5
    aux = j
    while i <= 9:
        aux = aux+2
        j = aux
        while j >= aux-2:
            print(f'I={i} J={j}')
            j-=1
        
        i+=2


main()
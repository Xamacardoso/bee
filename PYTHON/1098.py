def main():
    i = 0
    j = 1
    aux = 0.2
    while i<= 2:
        auxj = j+2
        while j<=auxj:
            if i == 0:
                print(f'I={i:.0f} J={j}')
            elif i == 1:
                print(f'I={i:.0f} J={j:.0f}')
            elif i >1.9:
                print(f'I={i:.0f} J={j:.0f}')
            else:
                print(f'I={i:.1f} J={j:.1f}')
                
            j+=1
        
        j = 1+aux 
        i+=0.2
        aux += 0.2


main()
def main():
    x, y = map(float,input().split())
    if x == 0:
        if y == 0:
            print('Origem')
        else:
            print('Eixo Y')

    elif y == 0:
        if x == 0:
            print('Origem')
        else:
            print('Eixo X')

    else:
        if x > 0 and y > 0:
            print('Q1')
        elif x > 0 and y < 0:
            print('Q4')
        elif x < 0 and y > 0:
            print('Q2')
        elif x < 0 and y < 0:
            print('Q3')

main()
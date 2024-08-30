come_diagonal = lambda x1,x2,y1,y2 : abs(x1 - x2) == abs(y1 -y2)
come_horizontal = lambda x1,x2 : x1 == x2
come_vertical = lambda y1,y2 : y1 == y2

def calcular_movimentos(x1,x2,y1,y2):
    if ([x1,y1]== [x2,y2]):
        return 0
    
    elif (come_horizontal(x1,x2) or come_vertical(y1,y2) or come_diagonal(x1,x2,y1,y2)):
        return 1

    return 2

def main():
    x1,y1,x2,y2 = map(int, input().split(' ')); 
    while x1 != 0 and x2 != 0 and y1 != 0 and y2 != 0: 
        print(calcular_movimentos(x1,x2,y1,y2));
        x1,y1,x2,y2 = map(int, input().split(' '));


main();
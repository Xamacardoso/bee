def main():
    n = int(input())
    count = 0
    
    while count<n:
        x, y = map(int, input().split(' '))
        if y == 0:
            print('divisao impossivel')
        else:
            print(f'{(x/y):.1f}')
        count+=1
    
main()
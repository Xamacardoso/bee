def main():
    count = 0
    n = int(input())
    while count<n:
        x, y = map(int, input().split(' '))
        maior = x if x>y else y
        menor = y+1 if x>y else x+1
        soma = 0
        while menor<maior:
            soma+=menor if menor%2 != 0 else +0
            menor+=1
        print(soma)
        count+=1
    
main()
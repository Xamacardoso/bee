def main():
    x = int(input())
    y = int(input())
    menor = x if x<y else y
    maior = x if x>y else y
    soma = 0
    while menor <= maior:
        soma += menor if menor % 13 != 0 else 0
        menor+= 1
    print(soma)
    
main()
p1001 = 1.50
p1002 = 2.50
p1003 = 3.50
p1004 = 4.50
p1005 = 5.50

n = int(input())
count = 1
soma = 0

while count <= n:
    cod, qtd = map(int, input().split(' '))
    if cod == 1001:
        soma += qtd*p1001
    elif cod == 1002:
        soma += qtd*p1002
    elif cod == 1003:
        soma += qtd*p1003
    elif cod == 1004:
        soma += qtd*p1004
    elif cod == 1005:
        soma += qtd*p1005

    count += 1

print(f'{soma:.2f}')

def main():
    n = int(input())
    count = 1
    soma = 0
    while count <= n:
        t, vm = map(int, input().split(' '))
        dist = t*vm
        soma += dist
        count += 1

    print(soma)
        

main()
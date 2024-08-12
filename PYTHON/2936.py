def main():
    soma = 225
    count = 1
    while(count<=5):
        n = int(input())
        if count == 1:
            soma += n*300
        elif count == 2:
            soma += n*1500
        elif count == 3:
            soma += n*600
        elif count == 4:
            soma += n*1000
        elif count == 5:
            soma += n*150
        count += 1

    print(soma)
    
main()
def main():
    x = int(input())
    fatorial = 1
    count = 1
    while(count<=x):
        fatorial *= count
        count+=1
    

    print(fatorial)


main()
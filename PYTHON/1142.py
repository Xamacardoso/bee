def main():
    n = int(input())
    count = 0
    aux = 1
    while count<n:
        print(f'{aux} {aux+1} {aux+2} PUM')
        aux += 4
        count+=1
    
main()
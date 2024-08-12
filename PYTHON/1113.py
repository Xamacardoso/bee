def main():
    x, y = map(int, input().split(" "))
    while x!=y:
        print('Decrescente') if x>y else print('Crescente')
        x, y = map(int, input().split(" "))
    

main()
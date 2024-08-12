def main():
    n = int(input())
    count = 1
    while count <= n:
        x, y = map(int, input().split(' '))
        raio = x+y
        print(raio)
        count += 1
        
main()
def main():
    x, m = map(int, input().split(' '))
    while x!=0 or m!=0:
        e = x*m
        print(e)
        x, m = map(int, input().split(' '))
    
main()
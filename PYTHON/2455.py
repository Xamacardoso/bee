def main():
    p1, c1, p2, c2 = map(int, input().split(' '))
    esq = p1 * c1
    dir = p2 * c2

    if esq > dir:
        print(-1)
    elif esq < dir:
        print(1)
    else:
        print(0)

main()
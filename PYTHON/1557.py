def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        for i in range(n):
            for j in range(n):
                valor = 2**(i+j)
                print("%{}d".format(len(str(4**(n-1)))) %(valor), end = '')
                if (j != n-1):
                    print(end = ' ')
            print()
        print()

main();
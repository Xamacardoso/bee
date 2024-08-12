def main():
    metros, comprimento = map(int,input().split(' '))
    termino = metros%comprimento
    print(termino)
    
main()
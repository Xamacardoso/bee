def main():
    competidores, papel, recebem = map(int, input().split(' '))
    if competidores * recebem <= papel:
        print('S')
    else:
        print('N')
    
main()
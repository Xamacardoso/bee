def main():
    alc = 0
    gas = 0
    dies = 0
    opcao = 0
    while opcao != 4:
        opcao = int(input())
        while opcao < 1 or opcao > 4:
            opcao = int(input())
        
        if opcao == 1:
            alc+=1
        elif opcao == 2:
            gas+=1
        elif opcao == 3:
            dies+=1

    print('MUITO OBRIGADO')
    print(f'Alcool: {alc}')
    print(f'Gasolina: {gas}')
    print(f'Diesel: {dies}')


main()
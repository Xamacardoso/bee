
def main():
    pressao_desejada = int(input())
    pressao_lida = int(input())
    diferenca = pressao_desejada - pressao_lida
    print(f'{diferenca:.0f}')

main()
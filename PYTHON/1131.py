def main():
    grenais, vit_inter, vit_gremio, empates = 0,0,0,0
    novo_grenal = 1
    while novo_grenal != 2:
        grenais += 1
        inter, gremio  = map(int, input().split(' '))
        if inter>gremio:
            vit_inter += 1
        elif gremio>inter:
            vit_gremio += 1
        elif gremio==inter:
            empates += 1
        print('Novo grenal (1-sim 2-nao)')
        novo_grenal = int(input())
        
    print(f'{grenais} grenais')
    print(f'Inter:{vit_inter}')
    print(f'Gremio:{vit_gremio}')
    print(f'Empates:{empates}')
    if vit_inter == vit_gremio:
        print('Nao houve vencedor')
    elif vit_inter>vit_gremio:
        print('Inter venceu mais')
    else:
        print('Gremio venceu mais')
        
main()
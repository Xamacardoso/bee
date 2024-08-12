def main():
    hi,mi,hf,mf = map(int,input().split(' '))
    if hi==hf and mi == mf:
        print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif hi<hf and mi<=mf:
        print(f'O JOGO DUROU {hf-hi} HORA(S) E {mf-mi} MINUTO(S)')
    elif hi<hf and mi>=mf:
        print(f'O JOGO DUROU {hf-hi-1} HORA(S) E {mf-mi+60} MINUTO(S)')
    elif hi == hf and mi < mf:
        print(f'O JOGO DUROU 0 HORA(S) E {mf-mi} MINUTO(S)')
    elif hi>=hf and mi<=mf:
        print(f'O JOGO DUROU {hf-hi+24} HORA(S) E {mf-mi} MINUTO(S)')
    elif hi>=hf and mi>mf:
        print(f'O JOGO DUROU {hf-hi+23} HORA(S) E {mf-mi+60} MINUTO(S)')

main()
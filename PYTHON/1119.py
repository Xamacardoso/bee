def main():
    tempo = int(input())
    horas = tempo//3600
    tempo = tempo - horas*3600
    mins = tempo//60
    segs = tempo%60
    print(f'{horas}:{mins}:{segs}')
    
main()
def main():    
    dias = int(input())
    anos = dias//365
    aux = dias - (anos*365)
    meses = aux//30
    dias = aux%30
    
    print(f'{anos} ano(s)')
    print(f'{meses} mes(es)')
    print(f'{dias} dia(s)')
    
main()
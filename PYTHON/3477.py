def main():
    pi = 3
    x,y,z = map(int, input().split())
    if x**2 == y**2 + z**2:
        areatriangulo= (z*y)/2
        areasemicirculo= (pi * (z/2)**2)/2
        areatotal = areatriangulo + areasemicirculo
        print(f'AREA = {areatotal:.0f}')
    else:
        print('Nao eh retangulo!')
    


main()
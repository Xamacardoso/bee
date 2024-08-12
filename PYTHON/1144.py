import math

def main():
    n = int(input())
    count = 1
    
    while count <= n*2:
        aux = math.ceil(count/2)
        if count % 2 == 1:
            print(f'{aux} {aux**2} {aux**3}')
        else:
            print(f'{aux} {aux**2+1} {aux**3+1}')
        count+=1
    
main()
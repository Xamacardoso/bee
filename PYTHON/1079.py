def main():
    n = int(input())
    count = 0
    while count < n:
        n1,n2,n3 = map(float, input().split(' '))
        media = (n1*2 + n2*3 + n3*5)/10
        print(f'{media:.1f}')
        count+=1
    
    
main()
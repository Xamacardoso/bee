def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        for i in range(n):
            for j in range(n):
                valor = abs(i - j) + 1
                
            
        
                
                print("%3d" %(valor), end = '')
                if (j != n-1):
                    print(end = ' ')
            print()
        print()
                
        
    
    
main();
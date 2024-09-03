def fib(n):
    lista = [0,]
    v1 = 0
    v2 = 1
    if n != 0:
        for i in range(1, n):
            aux = v1
            v1 = v2
            v2 = aux + v2
            lista.append(v1);
    
    print(*lista, sep= ' ');
    
    
def main():
    n = int(input());
    fib(n);
    
main();
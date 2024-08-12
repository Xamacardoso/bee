def main():
    lista = [];
    for i in range(10):
        num = int(input());
        lista.append(1) if num <= 0 else lista.append(num);

    for ind in range(10):
        print(f"X[{ind}] = ", lista[ind]);




main();
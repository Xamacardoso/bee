def main():
    while (True):
        try:
            rastro = input();
            processos_max = int(input());
            ciclos = 0;
            aux = 0;
            for index in range(len(rastro)):
                if rastro[index] == "W":
                    if aux > 0:
                        ciclos += 1;
                        aux = 0;
                    ciclos += 1;
                    continue;

                aux += 1;
                if aux == processos_max:
                    ciclos += 1;
                    aux = 0;
                    continue;

            ciclos += 1 if aux != 0 else 0;
            print(ciclos);

        except EOFError:
            break;

main();
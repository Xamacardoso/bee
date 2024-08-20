def computarCaso(proibido, num):
    stringNova = ''
    for index in range(len(num)):
        if num[index] == proibido:
            continue
        
        stringNova += num[index]

    return 0 if len(stringNova) < 1 or int(stringNova) == 0 else int(stringNova);


def main():
    numProibido, numContrato = input().split(" ");
    while numContrato != "0" and numProibido != "0":
        print(computarCaso(numProibido, numContrato));
        numProibido, numContrato = input().split(" ");


main();
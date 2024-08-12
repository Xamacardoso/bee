def main():
    casos = int(input());
    for caso in range(casos):
        string1, string2 = map(str, input().split(" "));
        resposta = ''
        for char in range(len(string1) + len(string2)):
            resposta += string1
        


main();
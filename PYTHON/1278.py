def exibir_elementos(lista):
    for index in range(len(lista)):
        print(lista[index]);

def texto_justificado(linha, maior):
    espacos = maior - len(linha);
    return (espacos * " ")+linha;

def tirar_espaco_meio(linha):
    string_formatada = "";
    for index in range(len(linha)):
        if (linha[index] == " " and linha[index +1] == " "):
            continue
        
        string_formatada += linha[index];
        

    return string_formatada;

def tam_maior_string(lista):
    maior = 0;
    for sequencia in lista:
        maior = len(sequencia) if len(sequencia) > maior else maior;
    
    return maior


def main():
    casos = int(input());
    check = 0;
    while (True):
        if casos == 0:
            break

        if check == 1:
            print()

        lista_strings = [];
        strings_formatadas = [];
        for caso in range(casos):
            entrada = input();
            lista_strings.append(tirar_espaco_meio(entrada.strip()));

        tamanho_linha_maior = tam_maior_string(lista_strings);
        for elemento in lista_strings:
            strings_formatadas.append(texto_justificado(elemento, tamanho_linha_maior));
        
        exibir_elementos(strings_formatadas);

        casos = int(input());
        check = 1;


main();
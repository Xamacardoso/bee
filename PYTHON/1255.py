def eh_letra(caractere):
    if (ord(caractere) >= 97 and ord(caractere) < 123):
        return True;
    
    return False;

def listar_letras(texto):
    listinha = [];
    for index in range(len(texto)):
        if texto[index] not in listinha:
            listinha.append(texto[index]);

    return listinha

def listar_frequencia_letras(texto, letras):
    frequencias = [];
    for letra in letras:
        if eh_letra(letra):
            count = 0;
            for caractere in texto:
                if caractere == letra:
                    count += 1;

            frequencias.append(count);

    return frequencias
    

def maior_valor_lista(listinha):
    maior = 0;
    for index in range(len(listinha)):
        maior = listinha[index] if listinha[index] > maior else maior;

    return maior


def exibir_frequentes(letras, frequencias, maior):
    mais_frequentes = "";
    for index in range(len(frequencias)):
        if frequencias[index] == maior:
            mais_frequentes += letras[index];

    return mais_frequentes;

def ordenar_string(texto):
    caracteres = list(texto);
    stringnova = "";
    n = len(caracteres)
    for i in range(n):
        for j in range(0, n-i-1):
            if caracteres[j] > caracteres[j + 1]:
                caracteres[j], caracteres[j+1] = caracteres[j+1], caracteres[j]

    for carac_ordenado in caracteres:
        stringnova += carac_ordenado;

    return stringnova;
    
def main():
    casos = int(input());
    for caso in range(casos):
        entrada = input().lower();
        letras = listar_letras(entrada);
        lista_frequencias = listar_frequencia_letras(entrada, letras);
        maior_freq = maior_valor_lista(lista_frequencias);
        letras_frequentes = ordenar_string(exibir_frequentes(letras,lista_frequencias,maior_freq));

        print(letras_frequentes)
        

main();
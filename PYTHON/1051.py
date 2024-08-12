def main():
    salario = float(input());
    taxas = [];
    if salario <= 2000.00:
        print("Isento");
        
    elif salario <= 3000.00:
        taxas.append((salario - 2000)*0.08);
        print(f"R$ {round(sum(taxas), 2):.2f}");
    elif salario <= 4500.00:
        taxas.append((salario - 3000)*0.18);
        taxas.append(1000 * 0.08);
        print(f"R$ {round(sum(taxas), 2):.2f}");
    elif salario > 4500.00:
        taxas.append((salario-4500)*0.28);
        taxas.append(1500 * 0.18);
        taxas.append(1000 * 0.08);
        print(f"R$ {round(sum(taxas), 2):.2f}");
    


main();
def main():
    cod1, num1, val1 = map(float, input().split());
    cod2, num2, val2 = map(float, input().split());
    
    print(f"VALOR A PAGAR: R$ {(num1*val1 + num2*val2):.2f}");
    
main();
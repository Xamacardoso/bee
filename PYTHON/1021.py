def main():
    valor = float(input())
    notas100 = valor // 100
    valor -= notas100*100
    notas50 = valor // 50
    valor -=notas50*50
    notas20 = valor // 20
    valor -=notas20*20
    notas10 = valor // 10
    valor -=notas10*10
    notas5 = valor // 5
    valor -=notas5*5
    notas2 = valor // 2
    valor -=notas2*2
    moedas1 = valor//1
    valor -= moedas1*1
    moedas50 = valor//0.5
    valor -= moedas50*0.5
    moedas25 = valor//0.25
    valor -= moedas25 * 0.25
    moedas10 = valor // 0.10
    valor -= moedas10*0.10
    moedas5 = valor//0.05
    valor -= moedas5*0.05
    print(valor)
    moedas1c = valor//0.009

    print(f'''NOTAS:
{notas100:.0f} nota(s) de R$ 100,00
{notas50:.0f} nota(s) de R$ 50,00
{notas20:.0f} nota(s) de R$ 20,00
{notas10:.0f} nota(s) de R$ 10,00
{notas5:.0f} nota(s) de R$ 5,00
{notas2:.0f} nota(s) de R$ 2,00
MOEDAS:
{moedas1:.0f} moeda(s) de R$ 1.00
{moedas50:.0f} moeda(s) de R$ 0.50
{moedas25:.0f} moeda(s) de R$ 0.25
{moedas10:.0f} moeda(s) de R$ 0.10
{moedas5:.0f} moeda(s) de R$ 0.05
{moedas1c:.0f} moeda(s) de R$ 0.01''')

main()
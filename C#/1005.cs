using System; 

class URI {

    static void Main(string[] args) { 

        // double (famoso float) a vai ser o valor de entrada;
        double a = double.Parse(Console.ReadLine());
        double b = double.Parse(Console.ReadLine());

        // O cifrao serve pra formatar a string, é parecido com o python
        // o ToString("0.00000") serve para limitar as casas decimais
        // enquanto transformando em string
        Console.WriteLine($"MEDIA = {((a*3.5+b*7.5)/11).ToString("0.00000")}");

    }

}
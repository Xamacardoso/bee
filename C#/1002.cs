using System;

class URI {
    static void Main(string[] args) {
        const double pi = 3.14159;
        double raio = double.Parse(Console.ReadLine());

        double area = pi * raio * raio;

        // Escreve com um limite de casas decimais
        Console.WriteLine($"A={area:0.0000}");
    }
}
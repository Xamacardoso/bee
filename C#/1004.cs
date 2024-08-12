using System; 

class URI {

    static void Main(string[] args) {
        /* Entrada de dados. int.Parse para transformar em inteiro
        (o valor é originalmente lido em string)
        */
        int a = int.Parse(Console.ReadLine());
        int b = int.Parse(Console.ReadLine());
        
        // Escreve PROD = numa linha, mas nao pula a linha toda.
        Console.Write("PROD = ");
        Console.WriteLine(a*b);
        
    }

}
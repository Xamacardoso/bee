using System; 

class URI {

    static void Main(string[] args) { 

        int num = int.Parse(Console.ReadLine());
        int horas = int.Parse(Console.ReadLine());
        double valor = double.Parse(Console.ReadLine());

        // $ é o formatador de string. o metodo tostring faz ele ficar com x casas decimais
        Console.WriteLine($"NUMBER = {num}");
        Console.WriteLine($"SALARY = U$ {(valor*horas).ToString("0.00")}");
    }

}
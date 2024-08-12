using System; 

class URI {

    static void Main(string[] args) { 

        String entrada = Console.ReadLine();
        String resposta = "mais";
        
        // verifica se a entrada é igual a uma dessas strings. || é o "or"
        if (entrada.ToLower() == "oposicao" ||
            entrada.ToLower() == "contrariedade"){
            resposta = "mas";
        }

        Console.WriteLine(resposta);
        
    }

}
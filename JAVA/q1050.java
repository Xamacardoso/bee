import java.io.IOException;
import java.util.Map;
import java.util.Scanner;
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class q1050 {
 
    public static void main(String[] args) throws IOException {
 
        Scanner in = new Scanner(System.in);
        // Map faz um dicionario
        // Integer e string tipam chave e valor
        // Map.of vai fazer um map(dicionario) a partir dos valores que eu inserir.
        Map<Integer, String> dicionario = Map.of(
            61, "Brasilia",
            71, "Salvador",
            11, "Sao Paulo",
            21, "Rio de Janeiro",
            32, "Juiz de Fora",
            19, "Campinas",
            27, "Vitoria",
            31, "Belo Horizonte"
        );
        int x = in.nextInt();

        // Getordefault vai pegar uma chave do dicionario, se ela nao existir retorna o default value ("DDD nao cadastrado")
        System.out.println(dicionario.getOrDefault(x,"DDD nao cadastrado"));
        in.close();
    }
 
}
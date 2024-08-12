import java.io.IOException;
import java.util.Scanner;
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class q1002 {
 
    public static void main(String[] args) throws IOException {
        
        Scanner in = new Scanner(System.in);
        double pi = 3.14159;
        double raio = in.nextDouble();

        System.out.println(String.format("A=%.4f",(Math.pow(raio, 2)*pi)));

        in.close();
    }
 
}
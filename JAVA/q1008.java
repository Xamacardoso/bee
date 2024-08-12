import java.io.IOException;
import java.util.Scanner;
public class q1008 {

    public static void main(String[] args) throws IOException {

        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int horas = in.nextInt();
        double valor = in.nextDouble();

        System.out.println(String.format("NUMBER = %d", num));
        System.out.println(String.format("SALARY = U$ %.2f", horas*valor));

        in.close();
    }
 
}


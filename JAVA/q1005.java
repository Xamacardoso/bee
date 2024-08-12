import java.io.IOException;
import java.util.Scanner;

public class q1005 {
      public static void main(String[] args) throws IOException {
        
        Scanner in = new Scanner(System.in);
        double nota1 = in.nextDouble();
        double nota2 = in.nextDouble();

        System.out.println(String.format("MEDIA = %.5f",((nota1*3.5 + nota2*7.5)/11)));

        in.close();
    }
}

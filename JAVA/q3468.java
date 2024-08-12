import java.io.IOException;
import java.util.Scanner;

public class q3468 {
      public static void main(String[] args) throws IOException {
        
        Scanner in = new Scanner(System.in);
        String entrada = in.nextLine();

        switch (entrada.toLowerCase()) {
          case "oposicao":
          case "contrariedade":
            System.out.println("mas");
            break;

          default:
            System.out.println("mais");
            break;

        }
        in.close();
    }
}

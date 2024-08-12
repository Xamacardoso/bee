import java.io.IOException;
import java.util.Scanner;

public class q3224 {
      public static void main(String[] args) throws IOException {
        
        Scanner in = new Scanner(System.in);
        String jon = in.nextLine();
        String medico = in.nextLine();

        if (jon.length() < medico.length()){
          System.out.println("no");
        }else{
          System.out.println("go");
        }

        in.close();
    }
}

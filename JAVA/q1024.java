import java.util.Scanner;

public class q1024{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();

        in.nextLine();
        for (int i = 0; i < num; i++){
            String entrada = in.nextLine();
            if (entrada.length() > 0 && entrada.length() < 1001){
                entrada = tresParaDireita(entrada);
                entrada = inverter(entrada);
                entrada = umParaEsquerda(entrada);
                System.out.println(entrada);
            }
        }

        in.close();
    }

    private static String tresParaDireita(String texto){
        String novo_texto = "";

        for (int i = 0; i < texto.length(); i++) {
            if (ehLetra(texto.charAt(i))){
                novo_texto += chr(ord(texto.charAt(i))+3);
                continue;
            }
            novo_texto += texto.charAt(i);
        }

        return novo_texto;
    }

    private static String inverter(String texto){
        String novo_texto = "";

        for (int i = texto.length()-1; i > -1; i--){
            novo_texto += texto.charAt(i);
        }

        return novo_texto;
    }

    private static String umParaEsquerda(String texto){
        int metade = Math.floorDivExact(texto.length(), 2);
        String texto_invertido = "";

        for (int i = 0; i < texto.length(); i++){
            if (i >= metade){
                texto_invertido += chr(ord(texto.charAt(i)) -1);
                continue;
            }
            texto_invertido += texto.charAt(i);
        }
        return texto_invertido;


    }

    private static boolean ehLetra(char caractere){
        return ord(caractere) > 64 && ord(caractere) < 91 || ord(caractere) > 96 && ord(caractere) < 123;
    }

    private static int ord(char caractere){
        return (int) caractere;
    }

    private static char chr(int codigo){
        return (char) codigo;
    }
}

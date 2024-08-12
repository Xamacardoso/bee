import java.util.Scanner;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;
public class q1040 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner in = new Scanner(System.in);
        String[] notaString = in.nextLine().split(" ");

        double[] notaDouble = Arrays.stream(notaString)
                                    .mapToDouble(Double::parseDouble)
                                    .toArray();

        List <Integer> arraypesos = Arrays.asList(2,3,4,1);
        double media = 0.0;
        for (int i = 0; i < arraypesos.size(); i++){
            media += arraypesos.get(i) * notaDouble[i];
        }

        /* stream pega uma lista e cria uma stream (sequencia de dados onde
        podemos iterar metodos ou funcoes), reduce pega um conjunto de dados e reduz ele a
        um unico valor, por meio da aplicação de uma função (0 é o valor inicial para o meu acumulador (acc), sum é meu acumulador, current é o elemento atual. a setinha é o retorno da função. nesse caso ele soma o sum com o valor atual que eu to percorrendo)*/
        media /= arraypesos.stream().reduce(0,(sum, current)->sum+current);
        System.out.println(String.format("Media: %.1f", media));
        
        String mensagem = "Aluno aprovado.";
        if (media < 5.0){
            mensagem = "Aluno reprovado.";
            System.out.println(mensagem);
        }else if (media < 7.0){
            mensagem = "Aluno em exame.";
            System.out.println(mensagem);
            System.out.print("Nota do exame: ");
            double notaexame = in.nextDouble();
            media = (notaexame + media) / 2;
            mensagem = "Aluno aprovado.";
            if (media < 5.0){
                mensagem = "Aluno reprovado.";
            }
            System.out.println(mensagem);
            System.out.println(String.format("Media final: %.1f", media));

        }else{
            System.out.println(mensagem);
        }
        

        in.close();
    }
}

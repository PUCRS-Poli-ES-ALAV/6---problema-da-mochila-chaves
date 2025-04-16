public class ex7 {
    int contador = 0; // Variável para contar as iterações

    int distEdProgDina(String A, String B) {
        int m = A.length();
        int n = B.length();
        int matriz[][] = new int[m+1][n+1];
        matriz[0][0] = 0; // matriz[0][0] = 0;
        for(int i = 1; i <= m; i++)
            matriz[i][0] = matriz[i-1][0] + 1; // soma uma I;
        for(int j = 1; j <= n; j++)
            matriz[0][j] = matriz[0][j-1] + 1; // soma uma R;
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                contador++; // Incrementa o contador a cada iteração
                int custoExtra;
                if(A.charAt(i-1) == B.charAt(j-1)) {
                    custoExtra = 0; // Operação M;
                } else {
                    custoExtra = 1; // Operação S;
                }
                matriz[i][j] = Math.min(matriz[i-1][j] + 1, 
                                        Math.min(matriz[i][j-1] + 1, 
                                        matriz[i-1][j-1] + custoExtra));
            }
        }
        return matriz[m][n];
    }

    public static void main(String[] args) {
        ex7 ed = new ex7();
        String A = "casablanca";
        String B = "portentoso";
        /* String A = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to "
         + "simplify the build processes in the Jakarta Turbine project. There were several "
         + "projects, each with their own Ant build files, that were all slightly different. "
         + "JARs were checked into CVS. We wanted a standard way to build the projects, a clear "
         + "definition of what the project consisted of, an easy way to publish project information "
         + "and a way to share JARs across several projects. The result is a tool that can now be "
         + "used for building and managing any Java-based project. We hope that we have created "
         + "something that will make the day-to-day work of Java developers easier and generally help "
         + "with the comprehension of any Java-based project.";

        String B = "This post is not about deep learning. But it could be might as well. This is the power of "
         + "kernels. They are universally applicable in any machine learning algorithm. Why you might "
         + "ask? I am going to try to answer this question in this article. "
         + "Go to the profile of Marin Vlastelica Pogančić. "
         + "Marin Vlastelica Pogančić Jun"; */
        
        // Medir o tempo de execução
        long inicio = System.nanoTime(); // Tempo inicial em nanossegundos
        int resultado = ed.distEdProgDina(A, B);
        long fim = System.nanoTime(); // Tempo final em nanossegundos

        // Calcular o tempo total em milissegundos
        double tempoExecucao = (fim - inicio) / 1_000_000.0;

        System.out.println("A distância de edição entre \"" + A + "\" e \"" + B + "\" é: " + resultado);
        System.out.println("Número de iterações: " + ed.contador); // Exibe o número de iterações
        System.out.println("Tempo de execução: " + tempoExecucao + " ms"); // Exibe o tempo de execução
    }
}
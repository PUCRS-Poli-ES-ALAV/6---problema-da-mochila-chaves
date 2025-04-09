# ED(S, T, i, j): int
# // S: String inicial, T: String final, i: [1..m], j:[1..n]
# // retorna o número mínimo de edições quando comparando
# // S[i] com T[j]. m é o tamanho de S, n o tamanho de T
# //
# Caso Base:
# Quando ficamos sem caracteres para comparer em S ou em T. Se em ambas,
#  o resultado é 0. Se uma das duas, retorna o restante dos caracteres da que nãoestá vazia;
# Casos Recursivos
# Se S[i] == T[i], chame recursivamente ED(S, T, i-1, j-1) (foi match,
#  nãoprecisa fazer nada nesta posição, o custo é zero.
# Se não, três chamadas recursivas são necessárias:
# • Substituição: ED(S, T, i-1, j-1) + 1
# • Inserção: ED(S, T, i, j-1) + 1
# • Remoção: ED(S, T, i-1, j) + 1
# • Retorne a que resultar em menor custo

contador = 0

def ED(S, T, i, j):
    global contador
    contador += 1
    # Caso base
    if i < 0:
        return j + 1
    if j < 0:
        return i + 1

    # Se os caracteres são iguais, não precisamos fazer nada
    if S[i] == T[j]:
        return ED(S, T, i - 1, j - 1)

    # Se os caracteres são diferentes, calculamos as três operações
    substituicao = ED(S, T, i - 1, j - 1) + 1
    insercao = ED(S, T, i, j - 1) + 1
    remocao = ED(S, T, i - 1, j) + 1

    # Retorna o mínimo entre as três operações
    return min(substituicao, insercao, remocao)

def main():
    global contador
    print("----------------------------------------------------------------------------------------------------")
    print("Exercício 6 - Distância de Edição")
    print("----------------------------------------------------------------------------------------------------")
    # S = input("Digite a string inicial: ")
    # T = input("Digite a string final: ")
    # S = "Casablanca"
    # T = "Portentoso"
    S = ("Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to "
     "simplify the build processes in the Jakarta Turbine project. There were several "
     "projects, each with their own Ant build files, that were all slightly different. "
     "JARs were checked into CVS. We wanted a standard way to build the projects, a clear "
     "definition of what the project consisted of, an easy way to publish project information "
     "and a way to share JARs across several projects. The result is a tool that can now be "
     "used for building and managing any Java-based project. We hope that we have created "
     "something that will make the day-to-day work of Java developers easier and generally help "
     "with the comprehension of any Java-based project.")
    T = ("This post is not about deep learning. But it could be might as well. This is the power of "
     "kernels. They are universally applicable in any machine learning algorithm. Why you might "
     "ask? I am going to try to answer this question in this article. "
     "Go to the profile of Marin Vlastelica Pogančić. "
     "Marin Vlastelica Pogančić Jun")
    print(f"S: {S}")
    print(f"T: {T}")
    i = len(S) - 1
    j = len(T) - 1
    resultado = ED(S, T, i, j)
    print(f"Resultado ED: {resultado}")
    print(f"Nmr interações: {contador}")

if __name__ == "__main__":
    main()
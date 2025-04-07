import time

def mochila(N, C, itens):
    maxTab = [[0] * (C + 1) for _ in range(N + 1)]
    iteracoes = 0
    instrucoes = 0

    for i in range(1, N + 1):
        for j in range(1, C + 1):
            iteracoes += 1
            peso, valor = itens[i]
            if peso <= j:
                maxTab[i][j] = max(maxTab[i-1][j], valor + maxTab[i-1][j - peso])
            else:
                maxTab[i][j] = maxTab[i-1][j]
            instrucoes += 3 

    return maxTab[N][C], iteracoes, instrucoes  


def main():
    casos_teste = [
        {
            "nome": "Caso 1",
            "C": 165,
            "pesos": [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            "valores": [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
        },
        {
            "nome": "Caso 2",
            "C": 190,
            "pesos": [56, 59, 80, 64, 75, 17],
            "valores": [50, 50, 64, 46, 50, 5]
        }
    ]

    print("Dinamico\n----------------------------------------------------------------------------------------------------")
    print("Test Case                  Result   Iterations Instructions     Time (s)")
    print("----------------------------------------------------------------------------------------------------")
    for caso in casos_teste:
        N = len(caso["pesos"])
        C = caso["C"]
        itens = [(0, 0)] + list(zip(caso["pesos"], caso["valores"]))

        inicio = time.time()
        valor_maximo, iteracoes, instrucoes = mochila(N, C, itens)
        fim = time.time()
        tempo = fim - inicio

        nome_formatado = f'{caso["nome"]} (N={N}, C={C})'
        print(f"{nome_formatado:<25} {valor_maximo:>6}    {iteracoes:>10}    {instrucoes:>11}     {tempo:.9f} s")

    print("----------------------------------------------------------------------------------------------------")

main()

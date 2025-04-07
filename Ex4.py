def mochila(N, C, itens):
    maxTab = [[0] * (C + 1) for _ in range(N + 1)]
    iteracoes = 0

    for i in range(1, N + 1):
        for j in range(1, C + 1):
            iteracoes += 1
            peso, valor = itens[i]
            if peso <= j:
                maxTab[i][j] = max(maxTab[i-1][j], valor + maxTab[i-1][j - peso])
            else:
                maxTab[i][j] = maxTab[i-1][j]

    return maxTab[N][C], iteracoes  


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

    for caso in casos_teste:
        N = len(caso["pesos"])
        C = caso["C"]
        itens = [(0, 0)] + list(zip(caso["pesos"], caso["valores"]))
        
        valor_maximo, iteracoes = mochila(N, C, itens)
        print(f"{caso['nome']}:")
        print(f"  Número de itens: {N}")
        print(f"  Capacidade: {C}")
        print(f"  Valor máximo: {valor_maximo}")
        print(f"  Iterações: {iteracoes}")
        print("-" * 40)

main()

# +--------+------------------+------------+----------------+------------+
# | Caso   | Número de Itens  | Capacidade | Valor Máximo   | Iterações  |
# +--------+------------------+------------+----------------+------------+
# | Caso 1 | 10               | 165        | 309            | 1650       |
# | Caso 2 | 6                | 190        | 150            | 1140       |
# +--------+------------------+------------+----------------+------------+


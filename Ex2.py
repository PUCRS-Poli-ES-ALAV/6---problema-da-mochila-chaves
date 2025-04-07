import time
import pandas as pd

def mochila_bruteforce(items, capacity):
    n = len(items)
    melhor_valor = 0
    melhor_combo = []
    iteration_counter = 0
    log = []
    start_time = time.time()

    def rec(i, peso_atual, valor_atual, combo_atual):
        nonlocal melhor_valor, melhor_combo, iteration_counter
        if i == n:
            iteration_counter += 1
            elapsed = (time.time() - start_time) * 1000  # tempo em milissegundos
            instruction = (f"Combinação {combo_atual} - Peso total: {peso_atual}, "
                           f"Valor total: {valor_atual}")
            log.append({"Iteração": iteration_counter,
                        "Tempo (ms)": round(elapsed, 2),
                        "Instrução": instruction})
            if peso_atual <= capacity and valor_atual > melhor_valor:
                melhor_valor = valor_atual
                melhor_combo = combo_atual.copy()
            return
        rec(i + 1, peso_atual, valor_atual, combo_atual)
        combo_atual.append(i)
        rec(i + 1, peso_atual + items[i][0], valor_atual + items[i][1], combo_atual)
        combo_atual.pop()

    rec(0, 0, 0, [])
    tempo_total = (time.time() - start_time)  # em segundos
    return melhor_valor, melhor_combo, iteration_counter, 3 * iteration_counter, tempo_total, log


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

    print("Bruteforce \n----------------------------------------------------------------------------------------------------")
    print("Test Case                  Result   Iterations Instructions     Time (s)")
    print("----------------------------------------------------------------------------------------------------")

    for caso in casos_teste:
        nome = caso["nome"]
        items = list(zip(caso["pesos"], caso["valores"]))
        C = caso["C"]
        N = len(items)

        valor_maximo, melhor_combo, iteracoes, instrucoes, tempo, log = mochila_bruteforce(items, C)

        nome_formatado = f'{nome} (N={N}, C={C})'
        print(f"{nome_formatado:<25} {valor_maximo:>6}    {iteracoes:>10}    {instrucoes:>11}     {tempo:.9f} s")

    print("----------------------------------------------------------------------------------------------------")


main()

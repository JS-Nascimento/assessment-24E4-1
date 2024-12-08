def knapsack(valores, pesos, capacidade):
    n = len(valores)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]


valores = [60, 100, 120]  # valores dos itens
pesos = [10, 20, 30]  # pesos dos itens
capacidade = 50  # capacidade maxima da mochila

resultado = knapsack(valores, pesos, capacidade)
print('o valor maximo é ' + str(resultado))

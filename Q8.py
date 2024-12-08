def selection_sort(jogadores):
    n = len(jogadores)
    for i in range(n):

        indice_menor = i
        for j in range(i + 1, n):

            if jogadores[j]['pontuacao'] < jogadores[indice_menor]['pontuacao']:
                indice_menor = j

        jogadores[i], jogadores[indice_menor] = jogadores[indice_menor], jogadores[i]

jogadores = [
    {"nome": "Jogador1", "pontuacao": 50},
    {"nome": "Jogador2", "pontuacao": 20},
    {"nome": "Jogador3", "pontuacao": 70},
    {"nome": "Jogador4", "pontuacao": 40}
]

selection_sort(jogadores)

print("Jogadores organizados por pontuação:")
for jogador in jogadores:
    print(jogador)

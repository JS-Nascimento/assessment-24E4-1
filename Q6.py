import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def medir_tempo_bubble_sort(tamanho_lista):
    lista = [random.uniform(1, 1000) for _ in range(tamanho_lista)]
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    return fim - inicio

tempo_1k = medir_tempo_bubble_sort(1000)
tempo_10k = medir_tempo_bubble_sort(10000)

resultado = {
    "Tempo para 1k elementos (s)": tempo_1k,
    "Tempo para 10k elementos (s)": tempo_10k,
    "Fator de aumento": round(tempo_10k / tempo_1k, 2)
}

import json
print(json.dumps(resultado, indent=4))


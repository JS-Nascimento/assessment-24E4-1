import random
# Impl da busca binaria
def busca_binaria(lista, isbn_procurado):
    inicio, fim = 0, len(lista) - 1
    iteracoes = 0
    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == isbn_procurado:
            return meio, iteracoes
        elif lista[meio] < isbn_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, iteracoes
# Impl da busca linear
def busca_linear(lista, isbn_procurado):
    iteracoes = 0
    for i, isbn in enumerate(lista):
        iteracoes += 1
        if isbn == isbn_procurado:
            return i, iteracoes
    return -1, iteracoes
# criando uma lista ordenada de 100 mil ISBNs
random.seed(42)
isbn_list = sorted(random.sample(range(1, 200000), 100000))
isbn_target = random.choice(isbn_list)
resultado_binaria, iteracoes_binaria = busca_binaria(isbn_list, isbn_target)
resultado_linear, iteracoes_linear = busca_linear(isbn_list, isbn_target)
resultado = {
    "ISBN Procurado": isbn_target,
    "Posição (Busca Binaria)": resultado_binaria,
    "Iterações (Busca Binaria)": iteracoes_binaria,
    "Posição (Busca Linear)": resultado_linear,
    "Iterações (Busca Linear)": iteracoes_linear
}
import json
print(json.dumps(resultado, indent=4))


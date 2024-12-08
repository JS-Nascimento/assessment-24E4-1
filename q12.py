import os
def listar_arquivos_recursivo(diretorio):
    arquivos = []
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isfile(caminho_completo):
            arquivos.append(caminho_completo)
        elif os.path.isdir(caminho_completo):
            arquivos.extend(listar_arquivos_recursivo(caminho_completo))
    return arquivos
diretorio_base = "C:/Engenharia_de_Software/algoritmos"
arquivos_encontrados = listar_arquivos_recursivo(diretorio_base)

for arquivo in arquivos_encontrados:
    print(arquivo)


from collections import deque
class SistemaAtendimento:
    def __init__(self):
        self.fila = deque()
    def adicionar_chamado(self, chamado):
        self.fila.append(chamado)
        print(f"Chamado '{chamado}' adicionado à fila.")
    def atender_chamado(self):
        if self.fila:
            chamado = self.fila.popleft()
            print(f"Atendendo chamado: {chamado}")
        else:
            print("Nenhum chamado na fila para atender.")

sistema = SistemaAtendimento()

sistema.adicionar_chamado("Chamado 1: Problema de conexão")
sistema.adicionar_chamado("Chamado 2: Erro no sistema")
sistema.adicionar_chamado("Chamado 3: Solicitação de suporte")

sistema.atender_chamado()  # Atende Chamado 1
sistema.atender_chamado()  # Atende Chamado 2
sistema.atender_chamado()  # Atende Chamado 3
sistema.atender_chamado()  # Fila vazia


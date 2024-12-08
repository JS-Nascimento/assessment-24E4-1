class Navegador:
    def __init__(self):
        self.historico = []
        self.futuro = []

    def visitar_pagina(self, pagina):
        self.historico.append(pagina)
        self.futuro.clear()
        print(f"Visitou: {pagina}")

    def voltar(self):
        if len(self.historico) > 1:
            pagina_atual = self.historico.pop()
            self.futuro.append(pagina_atual)
            print(f"Voltou para: {self.historico[-1]}")
        else:
            print("Não há páginas para voltar.")
    def avancar(self):
        if self.futuro:
            pagina_futura = self.futuro.pop()
            self.historico.append(pagina_futura)
            print(f"Avançou para: {pagina_futura}")
        else:
            print("Não há páginas para avançar.")
navegador = Navegador()
navegador.visitar_pagina("Página 1")
navegador.visitar_pagina("Página 2")
navegador.visitar_pagina("Página 3")
navegador.voltar()
navegador.voltar()
navegador.avancar()
navegador.visitar_pagina("Página 4")
navegador.avancar()
navegador.voltar()


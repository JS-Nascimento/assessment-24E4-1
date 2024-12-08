class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

def buscar_contato_por_nome(contatos, nome_procurado):
    for contato in contatos:
        if contato.nome.lower() == nome_procurado.lower():
            return contato.telefone  # retorna o numero de telefone correspondente.
    return "Contato não encontrado"  # retorna mensagem caso o nome nao seja encontrado.

contatos = [
    Contato("Ana", "1111-1111"),
    Contato("Bruno", "2222-2222"),
    Contato("Carlos", "3333-3333")
]

nome_procurado = "Bruno"
telefone = buscar_contato_por_nome(contatos, nome_procurado)
print(f"Resultado: {telefone}")

nome_procurado = "Jose"
telefone = buscar_contato_por_nome(contatos, nome_procurado)
print(f"Resultado: {telefone}")

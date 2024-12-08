class HashTable:
    def __init__(self):
        self.table = {}
    def adicionar_perfil(self, username, perfil):
        self.table[username] = perfil
    def buscar_perfil(self, username):
        return self.table.get(username, "Perfil não encontrado")
redesocial = HashTable()
usuarios = [
    {"username": "joao123", "nome": "João Silva", "idade": 25},
    {"username": "ana456", "nome": "Ana Costa", "idade": 30},
    {"username": "maria789", "nome": "Maria Oliveira", "idade": 22}
]
for usuario in usuarios:
    redesocial.adicionar_perfil(usuario["username"], usuario)
print("Recuperando perfis com hashtable:")
print(redesocial.buscar_perfil("joao123"))
print(redesocial.buscar_perfil("ana456"))
print(redesocial.buscar_perfil("naoexistente"))
def buscar_sequencial(lista, username):
    for usuario in lista:
        if usuario["username"] == username:
            return usuario
    return "Perfil não encontrado"
print("\nRecuperando perfis com busca sequencial:")
print(buscar_sequencial(usuarios, "joao123"))
print(buscar_sequencial(usuarios, "ana456"))
print(buscar_sequencial(usuarios, "naoexistente"))



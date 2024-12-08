def has_duplicates(lista):
    seen = set()
    for item in lista:
        if item in seen:
            return True
        seen.add(item)
    return False

lista = [1, 2, 3, 4, 5, 2]
print(f"Contém duplicatas? {has_duplicates(lista)}")

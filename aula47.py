"""
enumerete - enumera iteráveis (indices)
"""
lista = ['maria', 'helena', 'luiz']
lista.append('joão')

for indice,nome in enumerate(lista):
    print(indice,nome, lista(indice))

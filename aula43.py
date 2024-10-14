"""
 Cuidados com dados mutáveis
 = - copiando o valor (imutáveis)
 = - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['luiz', 'maria']
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)
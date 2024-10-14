"""
Lista em python
Tipos list - Mutável 
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamentos 
Métodos úteis:
    append, Insert, pop, del, clear, extend, +
Create Read Update   Delete
criar, ler, alterar, apagar = lista [i] (CRUD)
"""
#        0    1   2   3  
#       -4   -3  -2  -1
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
#EVITAR USAR(use apernas o final) A LISTA PARA MODIFICAÕES POI EXIGE MUITO PROCESSAMENTO
lista.append(50)
ultimo_valor = lista.pop() # remove o ultimo item da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(2)
print(lista, 'removido', ultimo_valor)
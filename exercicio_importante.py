lista = [1,2,3,4,5,6,7,8,9,10]

indice = input('digite o indice que você quer ver: ')

indices = range(len(lista))
int_indice = indice

if indice.isdigit():
    int_indice = int(indice)
    int_indice in indices
    print(f'Valor do item: {indice}, Item: {lista[int_indice]}')
else:
    print('numero caralho')
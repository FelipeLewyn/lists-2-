"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import  os

lista = []

while True:
    print('Selecione o que você deseja fazer')
    funcao_selecionada = input('[I]nserir [A]pagar [L]istar: ')

    if funcao_selecionada == 'i':
        os.system('clear')
        obejeto = input('O que você deseja adicionar: ')
        lista.append(obejeto)
    elif funcao_selecionada == 'a':
        indice_str = input(
            'Escolha o indice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
              print('Digite apenas números inteiros')
        except IndexError:
              print('Indice inexistente')
        except Exception:
              print('Erro desconhecido')

    elif funcao_selecionada == 'l':
        if len(lista) == 0:
             print('Não ha nada para mostrar')

        for l, objeto in enumerate(lista):
             print(l, objeto)
    else:
         print('por favor, escolha i, a ou l.')
    
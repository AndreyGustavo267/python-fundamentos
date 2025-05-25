# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from copy import deepcopy

def funcao_zipper(lista1, lista2):

    if len(lista1) < len(lista2):
        menor = deepcopy(lista1)
        maior = deepcopy(lista2)
    else:
        menor = deepcopy(lista2)
        maior = deepcopy(lista1)

    nova_lista = []

    for i, j in zip(menor, maior):  # Ou for i in range(len(menor))
        if i:
         nova_lista.append((i, j))

    return nova_lista

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

nova_lista = funcao_zipper(lista1, lista2)

print(nova_lista)
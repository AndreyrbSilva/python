lista = []

#L = list()

L = [12, 13, 14, 15]

L[0] = 10

print(L, "\n")

lista2 = L

print(L == lista2)

print(L is lista2, "\n")

lista2[0] = 1

print(lista2)
print(L, "\n")

lista3 = lista2.copy()
lista4 = lista2[:]

#Fatiamento

nova_lista = ['a', 'b', 'c', 'd', 'e', 'f'] #Intervalo Fechado

print(nova_lista[1:3])
print(nova_lista[0:4])

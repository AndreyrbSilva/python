#Criar a lista

minhaLista = [76, 92.3, "oi", True, 4, 76]
print(minhaLista, "\n")

#Inserindo valor "pitomba" e "76"

valor1 = "pitomba"
valor2 = 76

minhaLista = minhaLista + [valor1]
minhaLista = minhaLista + [valor2]

print(minhaLista, "\n")

#Inserindo o valor "Cibele" no índice 3

minhaLista = minhaLista[:3] + ["Cibele"] + minhaLista[3:]

print(minhaLista, "\n")

#Inserindo o valor "99" no início da lista

minhaLista = minhaLista[:0] + [99] + minhaLista[0:]

print(minhaLista, "\n")

#Encontrar o índice de "oi" na lista
indice_oi = -1

for i in range(1, 6):
    if minhaLista[i] == "oi":
        indice_oi = i
        break

if indice_oi != -1:
    print("O índice de 'oi' é:", indice_oi, "\n")
else:
    print("'oi' não encontrado na lista.\n")


#Removendo o True da lista

for i in range(0, 6):
    if minhaLista[i] is True:
        minhaLista[i] = "Nothing"
        break
        
print(minhaLista)

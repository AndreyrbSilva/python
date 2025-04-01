# 1. Desafio: Soma de Números
# Descrição: Crie um programa que solicite ao usuário dois números e exiba a soma entre eles.

# A váriavel recebe valores float para evitar erro em caso do usuario digitar números decimais.
num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))

# Recebe o valor das duas váriaveis, soma e armazena na váriavel "soma"
soma = num1 + num2 

# Imprime a váriavel "soma", o resultado da adição dos dois valores
print("A soma dos números é: ", soma)

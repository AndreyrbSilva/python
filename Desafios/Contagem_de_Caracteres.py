# Desafio: Contagem de Caracteres
# Descrição: Faça um programa que conte quantos caracteres existem em uma string informada pelo usuário.

# Pede ao usuário para digitar uma string
texto = input("Digite uma string: ")

# Conta o número de caracteres na string
# A função len() conta todos os caracteres, incluindo letras, números, espaços e pontuação.
# Exemplo: "Olá, mundo!" tem 12 caracteres (incluindo o espaço e a vírgula).
quantidade_caracteres = len(texto)

# Exibe o resultado
print("A quantidade de caracteres na string é: ", quantidade_caracteres)

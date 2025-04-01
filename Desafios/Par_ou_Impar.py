# 2. Desafio: Par ou Ímpar
# Descrição: Crie um programa que pergunte ao usuário um número e diga se ele é par ou ímpar.

# Criei um loop com o while para verificar se o usuário digita um valor decimal(float).
while True:
    # Pede ao usuário um número inteiro.
    num = input("Digite um valor inteiro: ")
    try:
        num = int(num) # Tenta converter o valor digitado para inteiro.
        break # Se a conversão for bem-sucedida, sai do loop e continua para a próxima etapa.
    except ValueError:
        # Caso o valor digitado não seja um número inteiro (exemplo: decimal ou texto),
        # o programa exibe uma mensagem de erro e solicita a entrada novamente.
        print("Erro! Tente novamente digitando um valor inteiro válido.\n")

# Etapa de verificação de par ou ímpar
# O operador % retorna o resto da divisão por 2. Se o resto for 0, o número é par.
if num % 2 == 0: # Verifica se o número é divisível por 2 sem resto (par).
    print("O numero digitado é par!") # Se o resto for 0, o número é par.
else:
    print("O numero digitado é impar!") # Se o resto não for 0, o número é ímpar.

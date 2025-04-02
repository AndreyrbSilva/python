# Atividade #
#LAB - Música Viva Mariana
#Resolver em três níveis

#1-for simples;
#2-for com diferenciação de singular e plural;
#3-estrutura completa com a complexidade do texto "é n", "é n+1".
# -------------------------------------- #

# Lista de contagens de 1 a 10
conta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Loop para percorrer cada número da lista 'conta'
for a in conta:
    # Se 'a' for 1, imprime um texto especial para o número 1
    if a == 1:
        print("\nMariana conta 1")  # Especifica que é a contagem de 1
        print("Mariana conta 1: é 1, é 1, é! \nAna, viva a Mariana, viva a Mariana")  # Texto para o caso específico de 1
    else:
        # Para os outros números, imprime "Mariana conta {a}"
        print("\nMariana conta", a)
        print("Mariana conta", a, end="")  # Inicia a sequência de 'é' na mesma linha
        print(": ", end="")
        # Loop para gerar a sequência de 'é {n}' até o número 'a'
        for b in range(1, a + 1):  # Vai de 1 até 'a'
            print("é", b, end=", ")  # Imprime cada número na sequência com "é" antes
        # Após o loop interno, imprime 'e' no final da sequência
        print("é")    
        # Mensagem de finalização
        print("Ana, viva a Mariana, viva a Mariana.")

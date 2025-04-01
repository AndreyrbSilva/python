num = int(input("Digite um número para ver sua tabuada: "))

print(f"\nA tabuada de {num} é:\n")
for i in range(1, 11):
    res = num * i
    print(f"{num} x {i} = {res}")
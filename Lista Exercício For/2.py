maior = 0 # variável para armazenar o maior número
for i in range(10):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero

print("O maior número é:", maior)

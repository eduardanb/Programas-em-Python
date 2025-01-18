n = int(input("Digite a quantidade de números: "))
soma = 0
menor = 0 # inicializa com o maior valor possível
maior = 0 # inicializa com o menor valor possível
contador = 0

while contador < n:
    numero = float(input("Digite um número: "))
    soma += numero
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero
    contador += 1

print("Menor valor:", menor)
print("Maior valor:", maior)
print("Soma dos valores:", soma)
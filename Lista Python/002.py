# Criando os vetores para armazenar os conjuntos
vetor_original = []
vetor_quadrado = []

# Lendo os valores do conjunto
print("Digite os valores do conjunto:")
for i in range(10):
    valor = float(input())
    vetor_original.append(valor)
    vetor_quadrado.append(valor ** 2)

# Imprimindo o conjunto original
print("Conjunto original:", vetor_original)

# Imprimindo o conjunto com os quadrados
print("Conjunto com quadrados:", vetor_quadrado)

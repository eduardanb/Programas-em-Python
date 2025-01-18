def soma_diagonal_secundaria(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        soma += matriz[i][n-i-1]
    return soma

# Obtendo a ordem da matriz do usuário
n = int(input("Digite a ordem da matriz: "))

# Lendo a matriz do usuário
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Calculando a soma dos elementos na diagonal secundária
soma = soma_diagonal_secundaria(matriz)

# Exibindo o resultado
print("A soma dos elementos na diagonal secundária é:", soma)
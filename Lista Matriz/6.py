def soma_abaixo_diagonal_principal(matriz):
    n = len(matriz)
    soma = 0
    for i in range(n):
        for j in range(i):
            soma += matriz[i][j]
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

# Calculando a soma dos elementos abaixo da diagonal principal
soma = soma_abaixo_diagonal_principal(matriz)

# Exibindo o resultado
print("A soma dos elementos abaixo da diagonal principal é:", soma)
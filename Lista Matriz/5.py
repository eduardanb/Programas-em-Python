# Solicitar ao usuário a ordem da matriz
n = int(input("Informe a ordem da matriz: "))

# Criar uma matriz vazia
matriz = []

# Solicitar ao usuário para inserir os valores da matriz
print("Insira os valores da matriz:")
for i in range(n):
    linha = []
    for j in range(n):
        valor = int(input(f"Insira o valor da posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz.append(linha)

# Calcular a soma dos elementos acima da diagonal principal
soma = 0
for i in range(n):
    for j in range(i + 1, n):
        soma += matriz[i][j]

# Imprimir a soma
print("A soma dos elementos acima da diagonal principal é:", soma)
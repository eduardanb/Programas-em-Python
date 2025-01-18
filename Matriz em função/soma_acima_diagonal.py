def ler_matriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            valor = int(input(f"Digite o valor da posição ({i}, {j}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calcular_soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            soma = soma + matriz[i][j]
    return soma

ordem = int(input('Insira a ordem da matriz: '))
matriz = ler_matriz(ordem)
soma_diagonal = calcular_soma_diagonal_principal(matriz)

for i in range(len(matriz)):
    print(matriz[i])

print('A soma é:',soma_diagonal)
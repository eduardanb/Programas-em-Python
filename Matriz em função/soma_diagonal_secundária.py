def soma_diagonal_secundária(matriz):
    soma = 0
    n = len(matriz)
    for i in range(len(matriz)):
            soma = soma + matriz[n-i-1][i]
    return soma

matriz = []
ordem = int(input('Informe a ordem da matriz: '))

for i in range(ordem):
    linha = []
    for j in range(ordem):
        valor = int(input(f"Digite o valor da posição ({i}, {j}): "))
        linha.append(valor)
    matriz.append(linha)
soma_ = soma_diagonal_secundária(matriz)

for i in range(len(matriz)):
    print(matriz[i])
print('Soma:',soma_)
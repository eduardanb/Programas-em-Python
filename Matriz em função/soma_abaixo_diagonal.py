def soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(i):
            soma = soma + matriz[i][j]
    return soma

matriz = []
ordem = int(input('Insira a ordem da matriz: '))

for i in range(ordem):
    linha = []
    for j in range(ordem):
        valor = int(input('Insira o valor da posição ({},{}): '.format(i,j)))
        linha.append(valor)
    matriz.append(linha)

soma_ = soma_abaixo_diagonal(matriz)

for i in range(len(matriz)):
    print(matriz[i])
print('A soma da diagonal principal é: ',soma_)
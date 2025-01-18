matriz = []

for i in range(3):
    linha = []
    for j in range(6):
        valor = float(input('Informe o valor da posição ({},{}): '.format(i,j)))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for j in range(1, 6, 2):
        soma_impar += linha[j]
print("Soma dos elementos das colunas ímpares:", soma_impar)

# Calculando a média aritmética dos elementos da segunda e quarta colunas
soma_segunda_quarta_coluna = 0
for linha in matriz:
    soma_segunda_quarta_coluna += linha[1] + linha[3]
media_segunda_quarta_coluna = soma_segunda_quarta_coluna / 6
print("Média aritmética da segunda e quarta colunas:", media_segunda_quarta_coluna)

# Substituindo os valores da sexta coluna pela soma das colunas 1 e 2
for i in range(3):
    matriz[i][5] = matriz[i][0] + matriz[i][1]

# Imprimindo a matriz modificada
print("Matriz modificada:")
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
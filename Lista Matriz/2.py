# Criar uma matriz vazia
matriz = []

# Solicitar ao usuário para inserir os valores da matriz
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Insira o valor da posição ({i+1}, {j+1}): "))
        linha.append(valor)
    matriz.append(linha)

# Solicitar ao usuário para inserir o valor a ser buscado
valor_busca = int(input("Insira o valor a ser buscado: "))

# Realizar a busca do valor na matriz
encontrado = False
linha_encontrada = -1
coluna_encontrada = -1

for i in range(5):
    for j in range(5):
        if matriz[i][j] == valor_busca:
            encontrado = True
            linha_encontrada = i
            coluna_encontrada = j

# Imprimir o resultado da busca
if encontrado:
    print(f"O valor {valor_busca} foi encontrado na posição ({linha_encontrada+1}, {coluna_encontrada+1}).")
else:
    print("O valor não foi encontrado na matriz.")
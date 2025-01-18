def contar_valores_maiores_que_10(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador = contador + 1
    return contador

matriz = []

for i in range(4):
    lista = []
    for j in range(4):
        valor = int(input('Informe o valor da posição ({} e {}): '.format(i,j)))
        lista.append(valor)
    matriz.append(lista)
valores_maiores_10 = contar_valores_maiores_que_10(matriz)
print(valores_maiores_10, 'valores maiores do que 10.')

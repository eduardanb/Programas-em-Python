lista = []

print('Informe os valores: ')
for i in range(10):
    valores = int(input())
    lista.append(valores)
print('Vetor:', lista)
maior_num = max(lista)
posicao = lista.index(maior_num)
print('O maior número é {}, e ele se encontra na posição {}.'.format(maior_num,posicao))
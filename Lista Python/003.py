lista = []
cont_par = 0
print('Informe os valores da lista: ')
for i in range(10):
    valor = int(input('Informe os valores: '))
    lista.append(valor)
    if valor % 2 == 0:
        cont_par = cont_par + 1
print('O vetor possui', cont_par,'valores pares.')
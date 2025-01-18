notas_validas = 0
soma_notas = 0

while notas_validas < 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        notas_validas += 1
        soma_notas += nota

media = soma_notas / 2
print("media = {:.2f}".format(media))
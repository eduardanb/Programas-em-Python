sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Valor inválido. Digite novamente.')

print('Sexo:', sexo)
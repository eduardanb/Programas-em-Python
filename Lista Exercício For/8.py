cont = 0
par = 0
impar = 0
for i in range(1,11):
    num = int(input('Informe o {}º valor: '.format(i)))
    cont = cont + num
    if num % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print('Em {} valores digitados pelo usuário, {} são pares.'.format(cont,par))
print('Em {} valores digitados pelo usuário, {} são ímpares.'.format(cont,impar))

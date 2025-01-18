usuario = int(input('Digite seu usuário: '))
senha = int(input('Digite sua senha: '))

while senha == usuario :
    senha = int(input('Senha inválida! Digite uma nova senha: '))
print('Sua senha é {}'.format(senha))
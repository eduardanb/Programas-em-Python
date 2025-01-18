hora_i = int(input(''))
hora_f = int(input(''))

if hora_i < hora_f:
    duracao = hora_f - hora_i
else:
    duracao = 24 - hora_i + hora_f
print('O JOGO DUROU {} HORA(S)'.format(duracao))


inicial, final = map(int, input().split())
if inicial < final:
    duraçao = final - inicial
else:
    duraçao= 24 - inicial + final
print(f'0 J0G0 DUROU {duraçao} HORAS(S)')
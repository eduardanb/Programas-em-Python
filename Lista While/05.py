n = int(input('Quatidade de alunos: '))
soma = 0
for i in range(n):
    n = int(input('Quatidade de alunos: '))
    soma = soma + n

media = soma / n
if media >= 0 and media <= 25:
    print('Turma Jovem')
elif media >= 26 and media <= 60:
    print('Turma Adulta')
else: 
    print('Turma Idosa')
print('Fim')
#Faça um programa para a leitura de duas notas parciais de um aluno. 
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem “Prova Final”, se a média alcançada estiver entre quatro e sete;
#A mensagem "Reprovado", se a média for menor do que quatro.

nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
media = (nota_1 + nota_2) / 2

if media >= 7:
    print("Sua média foi de:", media, "e você foi APROVADO!")
elif media >= 4 and media < 7:
    print("Sua média foi de:", media, "e você realizará a PROVA FINAL!")
else:
    print("Sua média foi de:", media, "e você foi REPROVADO!")
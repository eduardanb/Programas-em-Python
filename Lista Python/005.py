# Função para calcular o número de acertos de um aluno
def calcular_acertos(gabarito, respostas):
    acertos = 0
    for i in range(len(gabarito)):
        if gabarito[i] == respostas[i]:
            acertos += 1
    return acertos

# Leitura do gabarito da prova
gabarito = []
for i in range(10):
    resposta = input(f"Digite a resposta da questão {i+1}: ")
    gabarito.append(resposta)

# Leitura do número de alunos da turma
num_alunos = int(input("Digite o número de alunos da turma: "))

# Leitura dos cartões de respostas de cada aluno e cálculo do número de acertos
for i in range(num_alunos):
    aluno = input(f"Digite o número do aluno {i+1}: ")
    respostas_aluno = []
    for j in range(10):
        resposta = input(f"Digite a resposta da questão {j+1} do aluno {aluno}: ")
        respostas_aluno.append(resposta)
    acertos = calcular_acertos(gabarito, respostas_aluno)
    print(f"O aluno {aluno} acertou {acertos} questões.")
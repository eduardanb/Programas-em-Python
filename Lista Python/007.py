# Leitura dos dois vetores de números inteiros
vetor1 = []
vetor2 = []
for i in range(5):
    numero1 = int(input(f"Digite o {i+1}º número do primeiro vetor: "))
    vetor1.append(numero1)

for i in range(5):
    numero2 = int(input(f"Digite o {i+1}º número do segundo vetor: "))
    vetor2.append(numero2)

# Cálculo do vetor de diferenças
diferencas = [vetor1[i] - vetor2[i] for i in range(5)]

# Cálculo do vetor de somas
somas = [vetor1[i] + vetor2[i] for i in range(5)]

# Cálculo do vetor de multiplicação
multiplicacao = [vetor1[i] * vetor2[i] for i in range(5)]

# Impressão dos vetores calculados
print("Vetor de diferenças:", diferencas)
print("Vetor de somas:", somas)
print("Vetor de multiplicação:", multiplicacao)
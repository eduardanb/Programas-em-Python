print("Responda 'Sim' ou 'Não' para as seguintes perguntas:")

telefonou = input("Telefonou para a vítima? ")
local = input("Esteve no local do crime? ")
mora_perto = input("Mora perto da vítima? ")
devia = input("Devia para a vítima? ")
trabalhou = input("Já trabalhou com a vítima? ")

positivas = 0

if telefonou == "Sim":
    positivas += 1
if local == "Sim":
    positivas += 1
if mora_perto == "Sim":
    positivas += 1
if devia == "Sim":
    positivas += 1
if trabalhou == "Sim":
    positivas += 1

if positivas == 2:
    print("Você é suspeito.")
elif positivas == 3 or positivas == 4:
    print("Você é cúmplice.")
elif positivas == 5:
    print("Você é o assassino.")
else:
    print("Você é inocente.")

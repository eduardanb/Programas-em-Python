#Declaração da variável
var = input("Digite algo: ")

#Verificação doo tipo da variável
print("A informação é do tipo: ", type(var))

#Verifica se a informação possui letras e números
print("A informação possui letras e números?",var.isalnum())

#Verifica se a informação possui números
print("A informação é numérica?",var.isnumeric())

#Verifica se a informação é alfabética
print("A informação é alfabética?",var.isalpha())

#Verifica se têm somente espaços
print("A informação possui apenas espaços?",var.isspace())

#Verifica se a informação está em minúsculo
print("A informação está em minúsculo?",var.islower())

#Verifica se a informação está em maiúsculo
print("A informação está em maiúsculo?",var.isupper())

#Verifica se está capitalizada
print("A informação está capitalizada?",var.istitle())
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2

print("Sua parede têm dimensão de {} x {}, e sua área é de {}m².".format(largura,altura,area))
print("Para pintar a parede, você vai precisar de {}l de tinta.".format(tinta))
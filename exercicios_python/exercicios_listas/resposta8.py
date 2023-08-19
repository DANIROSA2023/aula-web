pessoas = []
for c in range(0,5):
    idade = int(input("Digite a " + str(c + 1) + "º idade: "))
    altura = float(input(f"Digite a {c + 1}º altura: "))
    pessoas.append([idade, altura])
pessoas.reverse()
print(pessoas)
notas = []


for i in range(0, 4):

   notas.append(float(input("Informe a nota do aluno: ")))


print(f"A média desse aluno é {sum(notas)/4}.")
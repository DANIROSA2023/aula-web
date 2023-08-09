
turno = str(input("Digite em que turno você estuda: M=maturnino, V=vespertino ou N-noturno:\n"))


if turno == "M" or turno == "m":
    print("Bom dia!")

elif turno == "V" or turno == "v":
    print("Boa tarde!")

elif turno == "N" or turno == "n":
    print("Boa noite!")

else:
    print("Valor inválido!")
    
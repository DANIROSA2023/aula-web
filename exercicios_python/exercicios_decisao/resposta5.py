nota1 = int(input("Digite a nota1:\n"))
nota2 = int(input("Digite a nota2:\n"))


media = (nota1 + nota2) / 2


if media >= 7 and media < 10:
    print("APROVADO \o/")

elif media >= 10:
    print("APROVADO COM DISTINÇÃO :D")

elif media > 3 and media <= 6:
    print("RECUPERAÇÃO :/")

else:
        print("Que pena! Você está em REPROVADO :(")

nota1 = float(input("Digite a nota 1:\n"))
nota_invalida = nota1 < 0 or nota1 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota1 = float(input("Digite a nota 1:\n"))
    nota_invalida = nota1 < 0 or nota1 > 10
print(f"Nota válida: {nota1}")

nota2 = float(input("Digite a nota 2:\n"))
nota_invalida = nota2 < 0 or nota2 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota2 = float(input("Digite a nota 2:\n"))
    nota_invalida = nota2 < 0 or nota2 > 10
print(f"Nota válida: {nota2}")

nota3 = float(input("Digite a nota 3:\n"))
nota_invalida = nota3 < 0 or nota3 > 10
while nota_invalida:
    print("A nota deve ser entre 0 (zero) e 10 (dez)")
    nota3 = float(input("Digite a nota 3:\n"))
    nota_invalida = nota3 < 0 or nota3 > 10
print(f"Nota válida: {nota3}")


media = (nota1 * 4 + nota2 * 5 + nota3 * 6) / 15

media_invalida = media < 0 or media > 10
aprovado = media >= 7
recuperacao = media > 3 and media < 7
reprovado = media < 3   


if media_invalida:
    print(f"Média Inválida -> {media}")
elif aprovado:
    print(f"Parabéns! Você está APROVADO com média {media}! \o/")
elif recuperacao:
    print(f"Quase! Você está em RECUPERAÇÃO com média {recuperacao} :|")
    #solicitar nota4
    #calcular nova media (media + 4 / 2)
    #testar a nova media agora com media 5
    nota4 = float(input("Digite a nota 4:\n"))
    media = (media + nota4) / 2
    aprovado = media >= 5
    if aprovado:
        print(f"Parabéns! Você está APROVADO com média {media}! \o/")
    else:
        print(f"Quase! Você está em RECUPERAÇÃO com média {reprovado} :(")

elif reprovado:
    print(f"Quase! Você está em RECUPERAÇÃO com média {reprovado} :(")

                     
                    
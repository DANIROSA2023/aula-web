
lista_de_numeros = range(3)
soma = 0
for numero in lista_de_numeros:
   nota = float(input(f"Digite a nota {numero + 1}:\n"))
   soma += nota

media = soma / len(lista_de_numeros)

print(f"Media: {media}")
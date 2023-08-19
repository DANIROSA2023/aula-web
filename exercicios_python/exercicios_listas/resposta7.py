# Uma lista com todos os números

numeros = []

# Onde está no loop

i = 0

# Loop apenas para voltar pro começo caso um número esteja inválido

while len(numeros) != 5:

   i += 1

   print("Diga o número " + str(i) + "º:")

   try:

       numero = int(input())

   except:

       print("Número inválido.")

       i -= 1

       continue

   numeros.append(numero)

   

# Mostrar os números

print("Números: " + ", ".join(str(numero) for numero in numeros))

# Para somar os números, use a função sum

soma = sum(numeros)

print("Soma: " + str(soma))

# Para multiplicar, faça um loop

multiplicacao = 1

for numero in numeros:

   multiplicacao = multiplicacao * numero

print("Multiplicação: " + str(multiplicacao))




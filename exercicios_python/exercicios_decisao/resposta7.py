numero1 = int(input("Numero1:\n"))
numero2  = int(input("Numero2:\n"))
numero3 = int(input("Numero3:\n"))

maior = numero1

if (numero2 > maior):
        maior = numero2
if (numero3 > maior):
        maior = numero3
print("Maior: ",maior)


menor = numero1

if (numero2 < menor):
        menor = numero2
if (numero3 < menor):
        menor = numero3
print("Menor: ",menor)
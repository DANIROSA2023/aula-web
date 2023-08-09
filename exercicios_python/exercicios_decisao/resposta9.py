numero1 = int(input("Digite o primeiro número:\n"))
numero2 = int(input("Digite o segundo número:\n"))
numero3 = int(input("Digite o terceiro número:\n"))


if numero1 < numero3:
    numero1, numero3 = numero3, numero1

if numero1 < numero2:
    numero1, numero2 = numero2, numero1

if numero2 < numero3:
    numero2, numero3 = numero3, numero2

print(f'A ordem decrescente é {numero1}, {numero2} e {numero3}')

    
 
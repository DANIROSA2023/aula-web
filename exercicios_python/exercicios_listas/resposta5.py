
x = 1
lista = []
print('Digite 20 números.')
while x <= 20:
    n = int(input("Digite um número: "))
    lista.append(n)
    x += 1
print('O maior valor é:',max(lista))
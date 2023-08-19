def imprimir_numeros_crescente(n: int):
    for i in range(1, n + 1):
        for _i in range(i):
            print(i, end= " ")
        print("")


print("numeros3")
imprimir_numeros_crescente(3)



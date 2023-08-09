produto1 = input("Produto1:\n")
produto2  = input("Produto2:\n")
produto3 = input("Produto3:\n")

mais_barato = produto1

if (produto2 < mais_barato):
        mais_barato = produto2
if (produto3 < mais_barato):
        mais_barato = produto3
print("Produto mais barato: ",mais_barato)
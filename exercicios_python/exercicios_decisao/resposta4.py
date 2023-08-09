vogais = ("a","e", "i", "o", "u")

letra = input("Digite uma letra do alfabeto:\n")
eh_vogal = letra.lower() in vogais

if eh_vogal:
    print("É vogal")
else:
    print("É consoante")
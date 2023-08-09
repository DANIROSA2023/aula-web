sexo = input("Digite sexo F ou M:\n")

if sexo == "F" or sexo == "f" or sexo == "M" or sexo == "m":
    if sexo == "F" or sexo == "f":
        print("Feminino")
    
    elif sexo == "M" or sexo == "m":
        print("Masculino")

else:
    print("Sexo Inválido")

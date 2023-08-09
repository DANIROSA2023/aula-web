nome = input("Digite nome de usuário:\n")
senha = input("Digite senha:\n")

invalido = nome == senha 

while invalido:
    print("Senha deve ser diferente de nome")
    nome = input("Digite nome de usuário:\n")
    senha = input("Digite senha:\n")
    invalido = nome == senha
print("Ok")
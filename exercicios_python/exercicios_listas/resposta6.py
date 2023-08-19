medias = list()

for aluno in range(10): soma_notas = 0

print(f"Notas do aluno {aluno+1}")

for nota in range(4): soma_notas += float(input(f"{nota+1}ª nota: "))

medias.append(soma_notas/4)

print()

aprovados = 0

for media in medias: 
    if media >= 7: aprovados += 1

print(f"{aprovados} aluno(s) com médias maiores ou iguais a 7,0")
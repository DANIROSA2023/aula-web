pop_a = int(input("Digite a população1 atual:\n"))
pop_b = int(input("Digite a população2 atual:\n"))
taxa_a = float(input("Digite a taxa1 atual:\n"))
taxa_b = float(input("Digite a taxa2 atual:\n"))
            
pop_a = pop_a
pop_b = pop_b
ano_passou = 0 

while pop_a < pop_b:

    ano_passou += 1
    mais_pop_a = pop_a * taxa_a // 100
    pop_a += mais_pop_a
    mais_pop_b = pop_b * taxa_b // 100
    pop_b += mais_pop_b

    if pop_a > pop_b:
        print(f"A população da cidadade A:{pop_a} habitantes passa a população da cidade B:{pop_b} habitantes após {ano_passou} anos.")
  

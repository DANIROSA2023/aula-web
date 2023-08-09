pop_a = 80000
pop_b = 200000
ano_passou = 0 

while pop_a < pop_b:

    ano_passou += 1
    mais_pop_a = pop_a * 3 // 100
    pop_a += mais_pop_a
    mais_pop_b = pop_b * 1.5 // 100
    pop_b += mais_pop_b

    if pop_a > pop_b:
        print(f"A população da cidadade A:{pop_a:.0f} habitantes passa a população da cidade B:{pop_b} habitantes após {ano_passou} anos.")
  

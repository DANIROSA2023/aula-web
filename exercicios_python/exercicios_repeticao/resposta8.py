
entered_number = int(input("Enter a number: "))
total = 0

for i in range(entered_number, 0, -1):
    print(i)
    total += i

average = total / (entered_number)

print("Total:", total)
print("Average:", average)
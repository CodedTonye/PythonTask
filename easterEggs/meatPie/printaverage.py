total = 0

for count in range(3):
    number = int(input(f"Enter integer {count+1}: "))
    total += number
   
average = total / 3

print (f"The average is {average:.2f}")

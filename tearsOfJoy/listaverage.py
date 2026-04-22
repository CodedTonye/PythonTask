numbers = [4, 8, 15, 16, 23, 42, 10, 5, 4, 7, 20]

total = 0
count = 0

for number in numbers:
    total += number
    count += 1
    
if count > 0:
    average = total / count
    print(f"Average is {average:.2f}")

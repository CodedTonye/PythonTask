numbers = []

for count in range(4):
    num = int(input(f"Enter an integer {count+1}: "))
    numbers.append(num)
    
total = sum(numbers)
average = total / len(numbers)
smallest = min(numbers)
largest = max(numbers)

product = 1
for number in numbers:
    product *= number
    
print(f"\nSum: {total}")
print(f"\nAverage: {average}")
print(f"\nProduct: {product}")
print(f"\nSmallest: {smallest}")
print(f"\nLargest: {largest}")

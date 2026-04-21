largest = -1
next_largest = -1

print("Enter 10 integers")

for count in range(10):
    number = int(input(f"Enter number {count+1}: "))
    
    if number > largest:
        next_largest = largest
        largest = number
        
    elif number > next_largest:
        next_largest = number
        
print(f"\nLargest: {largest}")
print(f"Second largest: {next_largest}")

        

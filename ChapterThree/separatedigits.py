number = int(input("Enter a five digit integer: "))

divisor = 10000

print("The digits are:", end=" ")

for count in range(5):
    digit = number // divisor
    print(digit, end=" ")
    
    number = number % divisor

    divisor = divisor // 10

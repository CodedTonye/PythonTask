def fahrenheit(c):
    return (9 / 5) * c + 32


print("Celsius  Fahrenheit")
print("-------------------")

for c in range(0, 101):
    f = fahrenheit(c)
    print(f"{c:3}  {f:9.1f}")

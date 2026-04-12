principal = float(input('Enter Principal amount: '))

annual_rate = float(input('Enter the annual interest rate %: '))

duration = float(input('Enter numbers of years: '))

r = annual_rate / (100 * 12)

n = duration * 12

monthly_rate = principal * (r * (1 + r)**n) / ((1 + r)**n - 1)

print('The monthly mortgage payment for the client is: $', monthly_rate)

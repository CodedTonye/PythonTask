principal = float(input('Enter Principal amount: '))

rate = float(input('Enter the annual interest rate: '))

time = float(input('Enter numbers of years: '))

simple_interest = (principal * rate * time) / 100

total_amount = principal * simple_interest

print('Simple interest:', simple_interest)
print('total_amount:', total_amount)

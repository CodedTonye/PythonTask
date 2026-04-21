principal = 120000

rate = 0.07

print(f"{'Year':>4} {'Balance':>10}")

for year in range(1, 31):
    amount = principal * (1 + rate) ** year
    
    print(f"{year:>4}    ${amount:>10,.2f}")

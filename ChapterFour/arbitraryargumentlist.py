def product(*args):
    result = 1
    for value in args:
        result *= value
    return result

print(product(2, 3))          
print(product(1, 2, 3, 4))    
print(product(5))             
print(product())              



import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input(f"Guess ({attempts + 1}/{max_attempts}): "))
    attempts += 1
    
    
    if guess < secret_number:
        print("-> Higher")
    elif guess > secret_number:
        print("-> Lower")
    else:
        print(f"-> Correct! ({attempts} attempts)")
        break
        
else:
    print(f"\nGame Over! You have used all {max_attempts} attempts.")
    print(f"The secret number was: {secret_number}")

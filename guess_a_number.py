import random

secret_number = random.randint(1, 100)
guess = 0

attempts = 0
max_attempts = 7

while attempts < max_attempts:
    print(f"Attempt - {attempts}")
    guess = int(input())
    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100")
        continue
    attempts += 1
    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print(f"Congrats!!! You win. You guessed {guess}")
if guess != secret_number:
    print(f"Sorry, you lose!!! Correct number was {secret_number}")
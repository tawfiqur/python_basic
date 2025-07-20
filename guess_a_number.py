guess_number = 23
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a two digit number: "))
    guess_count += 1
    if guess == guess_number:
        print('You guessed right!')
        break
else:
    print('Sorry, you didn\'t guess right!')
    print('Try again!')
    guess_limit = guess_count - 1


import random

random_number = random.randint(0, 100)
guess_count = 0

while True:
    guess = int(input("Guess the number: "))
    guess_count += 1
    
    if guess > random_number:
        print("TOO MUCH. TRY AGAIN")
        print()
    elif guess < random_number:
        print("TOO LOW. TRY AGAIN")
        print()
    else:
        print(f"CONGRATULATIONS. YOU GUESSED THE NUMBER IN {guess_count} GUESSES")
        break
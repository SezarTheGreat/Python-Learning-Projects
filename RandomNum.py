import random

low = int(input("Enter a low range: "))
high = int(input("Enter a high range: "))
guesses = 0

number = random.randint(low,high)

while True:
    guess = int(input(f"Enter a number between ({low} to {high}): "))
    guesses +=1

    if guess < number:
        print(f"{guess} is too low.")
    elif guess > number:
        print(f"{guess} is too high.")
    else:
        print(f"{guess} is correct.")
        break

print(f"This round took you {guesses} guesses.")
#Python number guessing game using random module
import random

low = 1
high = 100
guesses = 0

number = random.randint(low,high)
is_Running = True

print("PYTHON NUMBER GUESSING GAME")
if_True = input("Do you want to play this game (Y/N): ")

if if_True.lower() == 'y':
    while is_Running:
        guess =  input(f"Enter your guess between {low} and {high}: ")
        if guess.isdigit():
            guess = int(guess)
            guesses +=1
            
            if guess < low or guess > high:
                print("That number is out of range.")
                print(f"Please select a number between {low} and {high}: ")
            elif guess < number:
                print("Too low! Try again!")
            elif guess > number:
                print("Too High! Try Again!")
            else:
                print(f"Correct guess! The answer was {number}")
                print(f"Number of guesses: {guesses}")
                is_Running = False
        else:
            print("Invalid Guess.")
            print(f"Please select a number between {low} and {high}: ")
else:
    print("OK :((")

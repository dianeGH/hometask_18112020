import random

guess = random.randint(1,10)
print(guess)

user_input = input("Hi there, What is your name? ")
print("Welcome to our little game, " + user_input)

your_guess = int(input("Guess a number between 1 and 10 "))

too_low = str(guess-your_guess)
too_high = str(your_guess-guess)

if your_guess == guess:
    print("Well done " + user_input +  " you guessed the number!")
elif your_guess < guess:
    print("Sorry " + user_input +  " your guess was too low by " + too_low )
else:
    print("Sorry " + user_input +  " your guess was too high by " + too_high)

"""Here's what we're going to do... We're gonna input a number and let the computer generate a number randomly between 1 and 10. Then we're gonna guess it until it's correct. Ohh, we'll also let the computer give us hints about the numbers position also."""


import random

random_number = random.randint(1, 10)
your_guess = 0

while your_guess != random_number:
    your_guess = int(input("Input your guess, between 1-10: "))

    if your_guess < random_number:
        print("Sorry! Guess is lower than the number.")

    elif your_guess > random_number:
        print("Sorry! Guess is higher than the number.")

    else:
        print("Yay, You\'ve guessed the number!")
        break
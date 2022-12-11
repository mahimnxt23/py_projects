"""This is going to be a simple rock paper scissors game."""

import random

user = input('What\'s your choice? r=Rock, p=Paper, s=Scissors: ')
computer = random.choice(['r', 'p', 's'])

# player will win if r>s, s>p, p>r

if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
    print('You Win!')

elif user == computer:
    print('It\'s a tie.')

else:
    print('You Lose.')

print('---NUMBER GUESSER FROM 1-10---')

import random

def guess_number():
    min_num=1
    max_num=10
    random_number=random.randint(min_num,max_num)
    guess=0
    while guess != random_number:
        guess=int(input('Guess a number from 1-10: '))
        if guess<random_number:
            print('Too low. Guess again')
        elif guess>random_number:
            print('Too high. Guess again')
        else:
            print(f"Congrats! You have guessed the {random_number}")
            break

guess_number()
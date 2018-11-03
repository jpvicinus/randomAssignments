#3
#Write a program that generates a random number (between 1 and 10) and asks
#the user to guess what the number is.
#If the user’s guess is higher than the random number,
#the program should display “Too high, try again.” If the user’s
#guess is lower than the random number,
#the program should display “Too low, try again.”
#The program should use a
#loop that repeats until the user correctly guesses the random number.


import random

guess = int(input('Guess a number: '))
number = random.randint(1,10)
while guess is not number:

    if guess > number:
            print('Too high, try again.')

    if guess < number:
            print('Too low, try again.')

if guess == number:
            print('You got it!')

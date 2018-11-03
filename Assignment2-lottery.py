#1
#Write a Python program to play lottery.
#The program randomly generates a lottery of a two-digit number
#and prompt the user to enter two digits to play.
#Then the program determines whether the user wins according
#to the following rules:
#If the user input matches the lottery in exact order,
#the award is $20,000.
#If all the digits in the user input match all
#the digits in the lottery, the award is $10,000.
#If one digit in the user input matches a digit in the
#lottery, the award is $5,000.
#Otherwise, no award is granted.

import math
from random import randint

def random_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
random_digits = random_digits(2)

print('The random number is ',random_digits)
user = int(input('Enter a two digit number: '))
#random_digits = random_digits(2)

lottery_tens = random_digits // 10
lottery_ones = random_digits % 10
input_tens = user // 10 
input_ones = user % 10


#print (random_digits(2))

if user == random_digits:
    print('You have won $20,000!')
elif input_tens == lottery_ones and input_ones == lottery_tens:
    print('You have won $10,000!')
elif input_tens == lottery_ones or input_ones == lottery_tens or input_tens == lottery_tens or input_ones == lottery_ones:
    print('You have won $5,000!')
else:
    print('No award.')
print(' The lottery number is: ', random_digits)

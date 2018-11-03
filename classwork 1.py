#write a python program to ask the user to enter a number
#then your program should print if the number is odd
#or even


user_num = int(input('Enter a whole number: '))

if user_num % 2 == 0:
    print('That number is even.')
else:
    print('That number is odd.')

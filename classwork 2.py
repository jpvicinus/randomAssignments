#roulette wheel, the pockets are numbered from 0 to 18
#the colors of the pockets are:
#pocket 0 is green
#pocket 1 to 10, the odd numbered pockets are red and even are black
#pocket 11 to 18, the odd are black and even are red
#write a program to ask the user to enter a pocket number and display
#the corresponding color or error message otherwise



pocket = int(input('Enter a pocket number: '))


if pocket == 0:
    print('Green')
if pocket >= 1 and pocket <= 10 and pocket % 2 == 0:
    print('Red')
elif pocket >= 1 and pocket <= 10 and pocket % 2 > 0:
    print('Black')
if pocket >= 11 and pocket <= 18 and pocket % 2 == 0:
    print('Black')
elif pocket >= 11 and pocket <= 18 and pocket % 2 > 0:
    print('Red')
elif pocket > 18:
    print('Error.')


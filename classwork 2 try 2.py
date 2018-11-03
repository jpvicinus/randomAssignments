
pocket = int(input('Enter a pocket number: '))


if pocket == 0:
    print('Green')
if pocket >= 1 and pocket <= 10:
    if pocket % 2 == 0:
        print('Red')
    else :
        print('Black')
if pocket >= 11 and pocket <= 18:
    if pocket % 2 == 0:
        print('Black')
    else:
        print('Red')
if pocket > 18:
    print('Error.')


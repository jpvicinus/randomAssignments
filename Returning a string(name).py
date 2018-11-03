#this full_name function takes
#two strings as input parameters
#and returns the full name


def full_name(first,last):
    return first + ' ' + last

def main():
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter your last name: ')
    print('Your full name is ', full_name(first_name,last_name))

main()


#Write a Python Program to calculate the tax. Your program should have two functions
#1-tax function that calculates the tax according to the income using the following rules
#if the income is less than or equal to 10000 tax would be 10% of the income
#if the income is greater than 10000 and less than or equal to 30000 tax is 15%
#if the income is greater than 30000 tax is 25%
#2-The main function that prompts the user to enter his/her income,
#calls the tax function to get the corresponding tax value of the
#user's income and then displays the tax value


def UserInput():
    user_income = int(input('Enter your income'))
    return tax
def tax():
    if user_income <= 10000:
        print('the tax is 10%')
        print(user_income * .1)
    elif user_income > 10000 and user_income <= 30000:
              print('the tax is 15%')
              print(user_income * .15)
    else user_income > 30000:
              print('the tax is 25%')
              print(user_income * .25)
        return tax
def main():
    print(UserInput)
    print(tax)                
                    
                
main()

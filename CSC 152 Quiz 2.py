# Quz 2
# Write a program that calculates and displays a person's BMI
# BMI = weight * 703/height squared
# optimal if BMI is between 18.5 and 25
# underweight is if BMI is less than 18.5
# BMI over 25 the person is considereed overweight

#defining
height = float(input('Enter your height: '))
#height in inches
weight = float(input('Enter your weight: '))
#weight in pounds
sechalf = 703 / (height ** 2)
#this is the second half of the BMI calculation


#calculations
BMI = float(weight * sechalf)
#this calculates the BMI

#print statements
if BMI < 18.5:
    print('Your BMI is', BMI, 'and you are underweight.')
if BMI <= 25 and BMI >= 18.5:
    print('Your BMI is', BMI, 'and you are optimal weight.')
if BMI > 25:
     print('Your BMI is', BMI, 'and you are overweight.')





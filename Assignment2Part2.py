#Write a Python program that calculates the volume of a cylinder.
#The program should have 3 functions: 
#1 The first function prompts the user to enter
#the radius of a cylinder and the length 
#2 The second function does the following:
#Compute the volume using the following formulas:
    #area= radius* radius* (pi)
    #volume= area* length
    #For (pi), you can use the field in the math module (math.pi)
#3 The main function calls the first function to get the radius and the length of the cylinder,
#then use them to call the second function to calculate the cylinder ‘s area and volume and finally
#the main function displays both the area and the volume of the cylinder.



import math
#inputs go here


   # radius = float(input('Please enter a radius for the cylinder: '))
   # length = float(input('Please enter a length for the cylinder: '))

#setting up the functions to calculate the area and volume
def radius (num1, num2,num3):
    radius = float(input('Please enter a radius for the cylinder: '))
    result = num1 * num2 * num3
    return print(result(radius,radius,math.pi))
#area = multiply(radius,radius,math.pi)
#print(area)


def area(num1, num2):
    result = num1 * num2
    return result
#volume = multiply(area,length)
def volume(n1,n2):
    result = n1 * n2
    return volume(area,length)

def main():
    area =print('The area is: ', multiply(radius,radius,math.pi)
    volume =print('The volume is: ', multiply(area,length)
#print(volume)

#print statements
print('Your area is: ',area)
print('Your volume is: ',volume)

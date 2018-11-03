



def parameter_input():
    a = int(input('Please enter the value of a: '))
    b = int(input('Please enter the value of b: '))
    c = int(input('Please enter the value of c: '))
    d = int(input('Please enter the value of d: '))
    return a,b,c,d


def multiply(n1,n2):
    return n1*n2

def add(n1,n2):
    return n1 + n2

def divide(n1,n2):
    return n1/n2

#def isEven(n):
  #  return n % 2 == 0
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
# a * b + c / d and then tell whether it is odd or even
def main():
    a,b,c,d = parameter_input()
    product=multiply(a,b)
    sum=add(product,c)
    result = divide(sum,d)
    if is_even(result):
        print('Your result',result, 'is even')
    else:
        print('Your result',result, 'is odd')
    
main()


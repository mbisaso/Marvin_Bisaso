#the factorial of a number(5)

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
number = int(input('Enter a postive number :'))
    
if number < 0:
        print('please enter a postive number')
else:
        print('The factorial of', number, 'is', factorial(number))
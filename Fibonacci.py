import math

def Check_for_fibonacci(x):
    square_root= int(math.sqrt(x))
    return square_root*square_root==x

n=int(input('Enter any Number:  '))
num1 =5*(n*n)+4
num2 =5*(n*n)-4
if Check_for_fibonacci(num1) or Check_for_fibonacci(num2):
        print( f' Number {n} Is a Fibonacci Number')
else:
        print( f' Number {n} Is not a Fibonacci Number')


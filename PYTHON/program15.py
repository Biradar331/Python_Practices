# Program to find a factorial of a number using function
def fact(num):
    """
    Returns the factorial of a non-negative integer.
    Raises ValueError for negative numbers.
    """
    factorial=1
    if num < 0:
        raise ValueError("Factorial does not exist for negative numbers")
    elif num==0:
        return 1
    else:
        for i in range(2,num+1):
            factorial=factorial*(i)
        return factorial
result=fact(5)
print("The factorial of 5 is:", result)


# Python program to find the factorial of a number using Recursion

def fact(num):
    """
    Returns the factorial of a non-negative integer.
    Raises ValueError for negative numbers.
    """
    if num<0:
        raise ValueError ("The factorial of negative number doesn't exist")
    elif num==0:
        return 1
    else:
        return num*fact(num-1)
        
output=fact(5)
print("The factorial of 5 is:", output)


# Program to find the sum of first N natural numbers

def sum_n(N):
    """
    Returns the sum of first N natural numbers using recursion.
    """
    if N==0:
        return 0
    elif N<0:
        raise ValueError ("This Problem doesn't calculate the sum of negative numbers")
    return N+sum_n(N-1)
output=sum_n(10)
print("The sum of first 10 numbers is:", output)


# Write a recursive function that returns the sum of squares of the first N natural numbers.

def sum_of_squares(n):
    """
    Returns the sum of squares of first N natural numbers.
    """
    if n==0:
        return 0
    elif n<0:
        raise ValueError ("Can't calculate for negative numbers")
    return n**2+sum_of_squares((n-1))
result=sum_of_squares(3)
print(f"The sum of squares of first N natural numbers is {result}")
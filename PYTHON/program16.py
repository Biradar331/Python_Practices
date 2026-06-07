# Write a recursive function that returns the sum of all digits in a positive integer.

def sum_of_digits(n):
    if n<0:
        raise ValueError ("Input must be a non-negative integer")
    elif n==0:
        return 0
    else:
        remainder=n%10
    return sum_of_digits(n//10)+remainder
result=sum_of_digits(123)
print(f"The sum of digits are: {result}")
    
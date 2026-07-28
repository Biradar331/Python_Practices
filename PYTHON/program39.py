# python program to print sum of natural numbers up to n

def sum_nat (n):
    if n<=1:
        return n
    else:
        return (n) + sum_nat(n-1)

# Example usage
n = int(input("Enter a positive integer: "))

if n<=0:
    print("Please enter a positive integer.")
else:
    print (f'Sum of natural numbers up to {n} is: {sum_nat(n)}')
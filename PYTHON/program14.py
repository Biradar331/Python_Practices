# Program to find a factorial of a number

number=int(input("Enter a number:"))
factorial=1
if number<0:
    print("Factorial does not exist for negative numbers")
elif number==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, number+1):
        factorial=factorial*i
    print(f"The factorial of {number} is {factorial}")



# programt to find a factorial of a number using recursion
def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
factorial_of_number=factorial(5)
print(f"The factorial of 5 is {factorial_of_number}")



# Program to find factorial of a number using function

def factorial(number):
    factorial=1
    if number<0:
        print("Factorial does not exixt for negative numbers")
    elif number==0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, number+1):
            factorial=factorial*i
        print(f"The factorial of {number} is {factorial}")
factorial(5)


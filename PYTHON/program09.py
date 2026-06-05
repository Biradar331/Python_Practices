# Program to find largest number among three numbers

number1=float(input("Enter first number:"))
number2=float(input("Enter second number:"))
number3=float(input("Enter third number:"))
if number1>number2 and number1>number3:
    print(f"{number1} is the largest number")
elif number2>number1 and number2>number3:
    print(f"{number2} is the largest number")
else:
    print(f"{number3} is the largest number")


# program to find the largest number among three numbers
number1=float(input("Enter first number:"))
number2=float(input("Enter second number:"))
number3=float(input("Enter third number:"))
largest=number1
if number2>largest:
    largest=number2
if number3>largest:
    largest=number3
print(f"{largest} is the largest number")


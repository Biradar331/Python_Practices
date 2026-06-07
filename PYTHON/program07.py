# program to check if a number is positive, negative, or 0

# number=0
number = float(input("Enter a number:"))
if number >0:
    print("The number is positive")
elif number <0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")


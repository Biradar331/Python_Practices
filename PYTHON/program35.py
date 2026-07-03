# Python program to make a simple calculator

num1=float(input("Enter a first number:"))
num2=float(input("Enter a second number:"))

print(" Press 1 for addition \n press 2 for substaction \n press 3 for multiplication \n press 4 for division")

choice= int(input("Enter your choice:"))

if choice==1:
    print("The sum of", num1, "and", num2, "is:", num1+num2)
elif choice==2:
    print("The difference of", num1, "and", num2, "is:", num1-num2)
elif choice==3:
    print("The product of", num1, "and", num2, "is:", num1*num2)
elif choice==4:
    print("The quotient of", num1, "and", num2, "is:", num1/num2)
else:
    print("Invalid choice")

# Python program to make a simple calculator using functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1=float(input("Enter a first number:"))
num2=float(input("Enter a second number:"))
print("Press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")
choice=int(input("Enter your choice:"))

if choice==1:
    print("The sum of", num1, "and", num2, "is:", add(num1, num2))
elif choice==2:
    print("The difference of", num1, "and", num2, "is:", subtract(num1, num2))
elif choice==3:
    print("The product of", num1, "and", num2, "is:", multiply(num1, num2))
elif choice==4:
    print("The quotient of", num1, "and", num2, "is:", divide(num1, num2))
else:
    print("Invalid choice")

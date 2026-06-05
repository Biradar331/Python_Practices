# Program to check if a number is prime number or not

number=int(input("Enter the number:"))
if number<=1:
    print(f"{number} is not a prime number")
if number>1:
    for i in range(2,number):
        if number%i==0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime numer")
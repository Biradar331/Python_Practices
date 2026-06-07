# Program to check if a number is odd or even

# number=int(input("Enter a number:"))
number=int(13)
if number%2==0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
    

# Program to check leap year
year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Program-02 to check if a year is a leap year or not

year=int(input("Enter a year:"))
if (year%400==0) and (year%100==0):
    print(year, "is a leap year")
elif (year%4==0) and (year%100!=0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


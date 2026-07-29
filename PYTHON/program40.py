# python program to print N natural numbers in reverse order using for loop

N=int (input("Enter a positive number:"))
for i in range(N, 0, -1):
    print(i)


# Python program to calculate first N natural numbers

N=int(input("Enter a positive number:"))
sum=0
for i in range(0,N+1):
    sum=sum+i
print(sum)

# python program to calculate sum of numbers in a given range


def sum_of_given_range(start, end):
    n=end-start+1
    return ((n* (start+end))//2)
start=int(input("Enter a starting number:"))
end=int(input("Enter a ending number:"))
print(sum_of_given_range(start,end))


# Python program to check which year is a leap year and which one is not

def is_leap(year):
    return year%4==0 and year%100!=0 or year%400==0
year=int(input("Enter the year, you want to know is it a leap year or not:"))
print(is_leap(year))


# Python program to check the given number is a prime number or not

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
number=int(input("Enter a number to check is it a prime number or not: "))
print(is_prime(number))

# optimized prime number check in python

def is_prime (n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for i in range(3, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
number=int(input("Enter a number to check is it a prime number or not:"))
print(is_prime(number))
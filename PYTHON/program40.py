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

def is_it_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
number=int(input("Enter a number to check is it a prime number or not: "))
print(is_it_prime(number))

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

# python program to print all prime numbers in a given range

def print_prime_numbers(start, end):
    for num in range(start, end+1):
        if num<=1:
            print("Enter a number greater than 1")
        elif num>1:
            for i in range(2, int(num**0.5)+1):
                if num%i==0:
                    break
                else:
                    print(f"the prime numbers between {start} and {end} are : {num}")

start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
print_prime_numbers(start, end)


##2

def get_primes_in_range(start, end):
    primes=[]
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    return primes

# python progrsm to extarct digits from a number and calculate sum of digits

num=int(input("Enter a number to extract digits and calculate sum of those digits:"))
n=num
sum=0
while (n>0):
    remainder=n%10
    sum=sum+remainder
    n=n//10
print(sum)

# pthon program to extarct digits and calculate their sum using function

def sum_digits(n):
    total=0
    while n>0:
        total=total+(n%10)
        n=n//10
    return total
sum_digits(123)
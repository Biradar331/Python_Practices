# python program to check if a number is palindrome or not

n=int(input("Enter a number:"))
num=n
result=0

while num>0:
    last_digit=num%10
    result=(result*10) +last_digit
    num=num//10

if result==n:
    print("The given number",n, "is a palindrome")
else:
    print("the given number", n, "is not a palindrome")

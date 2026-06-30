# python program to find the factorials of a number

from math import sqrt
result=[]

num=int(input("Enter a number to find the factors of it:"))
for i in range(1, int (sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i != 0:
            result.append(num//i)

print(result)
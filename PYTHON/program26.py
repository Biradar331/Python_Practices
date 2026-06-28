# python program to calculate the sum of n natural numbers

num=int(input("Enter a natural number:"))

sum=0
temp=num
if temp<0:
    print("Enter a positive number:")
else:
    while temp>0:
        sum=sum+temp
        temp=temp-1

print(sum)
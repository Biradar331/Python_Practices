# Python program to writa a fibonacci sequence using for loop

num=int(input("Enter a number:"))
a=0
b=1
print(a)
print(b)

for i in range(1,num+1):
    c=a+b
    a=b
    b=c
    print(c)



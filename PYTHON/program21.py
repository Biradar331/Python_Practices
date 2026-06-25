# Python program to writa a fibonacci sequence using for loop

num=int(input("Enter a number:"))
a=0
b=1

if num<=1:
    print(a)
else:
    print(a)
    print(b)

    for i in range(3,num+1):
        c=a+b
        a=b
        b=c
        print(c)




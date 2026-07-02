# Program to find numbers divisible by another number

num=int(input("Enter a number:"))
for i in range(1, 101):
    if i%num ==0:
        print(i)
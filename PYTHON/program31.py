# Program to find numbers divisible by another number using for loop

num=int(input("Enter a number:"))
for i in range(1, 101):
    if i%num ==0:
        print(i)


# Solution 2 using lambda function or filter()

num=int(input("Enter a number:"))
divisible_numbers = list(filter(lambda x: x % num == 0, range(1, 101)))
print(divisible_numbers)
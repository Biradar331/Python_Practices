# Python program to find the factors of a number using for loop

num=int(input("Enter a number:"))
print("The factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# Python program to find the factors of a number using while loop
num=int(input("Enter a number:"))
print("The factors of", num, "are:")
i=1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1


# Python program to find the factors of a number using recursion
def factors(n, i=1):
    if i > n:
        return
    if n % i == 0:
        print(i)
    factors(n, i + 1)

num=int(input("Enter a number:"))
print("The factors of", num, "are:")
factors(num)
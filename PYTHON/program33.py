# Python program to find HCF (Highest Common Factor) / GCD (Greatest Common Divisor) of two numbers using loop

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the smaller number
if num1 > num2:
    smaller = num2
else:
    smaller = num1

# Find the HCF/GCD
hcf = 0
for i in range(1, smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        hcf = i

print("The HCF/GCD of", num1, "and", num2, "is", hcf)


# python program to find HCF/GCD of two numbers using def function
def HCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1, smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
    return hcf
print("The HCF/GCD of 12 and 30 is", HCF(12,30))

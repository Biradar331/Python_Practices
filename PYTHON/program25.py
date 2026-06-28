# python program to check if a number is a armstrong number or not

n=int(input("Enter a number:"))
num=n
result=0

while num>0:
    ld=num%10
    result=result+ld**len(str(n))

    num=num//10
if n==result:
    print(f"The number {n} is a armstrong number")
else:
    print(f"The number {n} is not a armstrong number")

## Time complexisty for the above problem is --> O(log10(n))


# Python program to check if a number is armstrong number or not in an interval

lower=int(input("Enter a lower limit:"))
upper=int(input("Enter a upper limit:"))


for num in range(lower, upper+1):
    result=0
    temp=num
    order=len(str(num))
    while temp>0:
        digit= temp%10
        result= result+digit**order
        temp=temp//10
    if num==result:
        print(num)

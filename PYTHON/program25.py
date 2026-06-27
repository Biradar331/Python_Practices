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

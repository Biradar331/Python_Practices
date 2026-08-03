# python program to reverse a number using loop

n=int(input("Enter a number:"))
num=n
reverse=0
while num>0:
    reverse=reverse*10+(num%10)
    num=num//10
print(reverse)
    
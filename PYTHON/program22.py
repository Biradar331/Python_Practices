# Python program to check if the number is armstrong number or not for 3 digit number only

num=int(input("Enter a number here:"))
sum=0
temp=num

while temp>0:
    digit=temp%10
    cube= digit **3
    sum=sum+cube
    temp=temp//10

if sum==num:
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")


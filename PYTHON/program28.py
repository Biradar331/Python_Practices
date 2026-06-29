# Python program to print all factors of a given number

result=[]
num=int(input("Enter the number:"))
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print(result)
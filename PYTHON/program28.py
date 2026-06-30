# Python program to print all factors of a given number using loop condition

result=[]
num=int(input("Enter the number:"))
for i in range(1,num+1):
    if num%i==0:
        result.append(i)
print(result)

# Time Complexity would be : O(N) & Space complexity would be O(K) 'k' would be total no. of factors

# python program to print all factors of a number 

result=[]
num=int(input("Enter the number:"))
for i in range(1,(num//2)+1):
    if num%i==0:
        result.append(i)
result.append(num)
print(result)
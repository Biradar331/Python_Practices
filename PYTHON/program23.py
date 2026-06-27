# python program to extract the number of digits from a number using loop

n=1234
num=n
while num>0:
    digit=num%10
    print(digit)
    num=num//10
    

# python program to count the number of digits from an integer

n=int(input("Enter a number:"))
num=n
count=0
while num>0:
    digit=num%10
    count+=1
    num=num//10
print("The count of digits present in a given number",n, "are",count)
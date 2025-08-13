#to find the factorial of a first n numbers using for loop

n=5
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
    print("factorial is:",fact)
    
    
# output: it will print the factorial of 5


# now by using for loop

n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
    print("factorial is:",fact)
    
    
    
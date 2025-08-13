# Break and Continue statements in while loops
# Break statement used to termminate a loop when encountered

i=1
while(i<=10):
    i += 1
    if(i==6):
        break
    print(i)
    
# It will print the numbers from 1 to 5 only because we have used break statement after if statement


# Continue Statement in while loop 
# Continnue statement used to "Terminate execution in the current iteration and continues the execution of the loop with the next iteration"
# Continue statement acts as "skip"
print("question 02")
i=0
while(i<=10):
    if(i==7):
        i+=1
        continue #skip
    print(i)
    i+=1
    
 # Ie was skiooing the number 7
 
 #Q3
print("question 03")
i=1
while(i<=10):
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

# So it will only odd numbers


print("question 04")
i=1
while(i<=10):
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1

# It will print Even numbers


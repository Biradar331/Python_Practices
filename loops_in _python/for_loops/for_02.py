#print the elements of the following list using a for loop [1,4,9,16,25,36,49,64,81,100]

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)
    
#output: It will print all the elements in the list


#search for a number x in this tuple using for loop


print("question 02")


tup=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
for el in tup:
    if(el==x):
        print("element found at index:",idx)
    else:
        print("element not found")
    idx+=1

#output: It will find the index of the perticular number given input by the user

#By using break statement 

print("question 03")


tup=(1,4,9,16,25,36,49,64,81,100)
x=36
idx=0
for el in tup:
    if(el==x):
        print("element found at index:",idx)
        break
    else:
        print("element not found")
    idx+=1



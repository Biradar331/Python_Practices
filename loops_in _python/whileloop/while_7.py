#Search for number x in this tuple using while loop (1,4,9,16,25,36,49,64,81,100)

nums=(1,4,9,16,25,36,49,64,81,100)
idx=0
n=int(input("enter the number you want to search:"))
while(idx<len(nums)):
    if(nums[idx]==n):
        print("number found",nums[idx], "at index",idx)
    else:
        print("finding.......",nums[idx],idx)   
    idx+=1

#it will find the fixed number, the input taken from the user






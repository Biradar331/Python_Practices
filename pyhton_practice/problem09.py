#sum of 1 to 10 using recursion and without using return function
def sumofnum(sum,i,n):
    if i>n:
        print(sum)
        return
    sumofnum(sum+i,i+1,n)
sumofnum(0,1,10)

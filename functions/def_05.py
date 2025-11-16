def func(sum,i,N):
    if i>N:
        print(sum)
        return sum
    return func(sum+i,i+1,N)
result=func(sum=0,i=1,N=5)
print("sum of numbers from 1 to",5,"is",result)

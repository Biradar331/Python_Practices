# python program to display powers of 2 using anonymous function

nterms=int(input("enter number of terms here:"))

result= list(map(lambda x: 2**x, range(nterms+1)))

for i in range (nterms+1):
    print("The value of 2 raised to power", i, "is", result[i])
    
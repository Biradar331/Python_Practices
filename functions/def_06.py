def factorial(N,result):
    if N==0:
        print(result)
        return
    return factorial(N-1,result*N)
factorial(5,1)
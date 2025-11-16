#problem  01


def func(N):
    if N==1:
        return 1
    return N*func(N-1)
N=6
print("factorial of",N,"is", func(N))




#problem 02
def factorial(N):
    # Base case: factorial of 0 or 1 is 1
    if N == 0 or N == 1:
        return 1
    
    # Recursive case
    return N * factorial(N - 1)

# Example
N = 5
print("Factorial of", N, "is:", factorial(N))

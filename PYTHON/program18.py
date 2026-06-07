# Program to find power of a number by taking two parameters using recursion

def pow_num(x,n):
    if x==0 and n>=1:
        return 0
    if x>=1 and n==0:
        return 1
    if n<0:
        raise ValueError("Negative exponents are not supported")
    return x*pow_num(x,n-1)
result=pow_num(8,3)
print(f"the power of a number would be:",result)
# program to calculate the product of positive digits using recursion

def product_digits(n):
    if n<0:
        raise ValueError ("Can't calculate for negative digits")
    if n==0:
        return 0
    if n<10:
        return n
    return (n%10)*product_digits(n//10)
result=product_digits(1234)
print("the product of given digits are:", result)

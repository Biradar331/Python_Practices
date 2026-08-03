def sum_digits(n):
    total=0
    while n>0:
        total=total+n%10
        n=n//10
    return total
answer=sum_digits(123)
print(answer)
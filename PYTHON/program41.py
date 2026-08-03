def is_prime (n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        for i in range(3, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
number=int(input("Enter a number to check is it a prime number or not:"))
print(is_prime(number))

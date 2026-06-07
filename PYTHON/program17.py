# Write a recursive function to count the number of digits in a positive integer.

def count_digits(n):
    if n<10:
        return 1
    return 1+count_digits(n//10)
result=count_digits(123456765487908765433456432345678934658)
print(f"The count of digits given are:{result}")
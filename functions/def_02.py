#problem 2 on def function
def check_even_odd(num):
    i = num
    while i <= num:  # Loop runs only once
        if i % 2 == 0:
            print(i,"is Even")
        else:
            print(i, "is Odd")
        i += 1  # Increment so loop stops

number = int(input("Enter a number: "))
check_even_odd(number)
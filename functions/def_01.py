#Q0 1

def print_odev(n):
    if(n%2==0):
        print("the number is even")
    else:
        print("the number is odd")
print_odev(34)

#Q02

def print_odev(n):
        if(n%2==0):
            print("the number is even")
        else:
            print("the number is odd")
print_odev(65)

#Q03

def check_even_odd(num):
    for i in range(num,num+1):
        if(i%2==0):
            print("the number is even",i)
        else:
            print("the number is odd",i)
number=int(input("enter a number:"))
check_even_odd(number)
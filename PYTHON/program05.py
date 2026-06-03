# program to swap two variables using third variable
a=5
b=10
print("before swapping a=",a,"b=",b)
temp=a
a=b
b=temp
print("after swapping a=",a,"b=",b)


# program to swap two numbers without using third variable
a=6
b=8
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping a=",a, "b=",b)

# program to swap two numbers without using third variable
a=12
b=23
print("before swapping a=", a, "b=",b)
a=a*b
b=a/b
a=a/b
print("after swapping a=",a,"b=",b)


# program to swap two numbers without using third variable
a=15
b=25
print("before swapping a=",a,"b=",b)
a,b=b,a
print("after swapping a=",a,"b=",b)

# python program to extract the number of digits from a number using loop

n=1234
num=n
while num>0:
    digit=num%10
    print(digit)
    num=num//10
    

#Write a program to check if a list contains a palindrome of elements (Hint:use copy()method)

list=[1,2,3,4,3,1]
list1=list.copy()
list1.reverse()

if list1 == list :
    print("palindrome")
else:
    print("not a palindrome")
    

#check if a string is palindrome or not? using while loop

from ast import And

def check_palindrome(s,left,right):
    while left<=right:
        if s[left]!=s[right]:
            return "Not a palindrome"
        left+=1
        right-=1
    return "palindrome"
s="abcddcbc"
print(check_palindrome(s,0,len(s)-1))

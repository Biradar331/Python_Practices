def check_palindrome(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return check_palindrome(s,start+1,end-1)
s="NITIA"
x=check_palindrome(s,0,len(s)-1)
print(x)
    
    
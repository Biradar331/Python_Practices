# To print numbers from 1 to N by using recursion
def func(i,n):
    if i<n:
        return
    func(i-1,n)
    print(i)
func(5,1)
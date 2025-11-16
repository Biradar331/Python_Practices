def func(N):
    if N==1:
        return 1
    return N+func(N-1)
func(4)
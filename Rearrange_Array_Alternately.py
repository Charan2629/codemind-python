def rearrange(A, N):
    temp = N*[None]
    low, high = 0, N - 1
 
    flag = True
 
    for i in range(N):
        if flag is True:
            temp[i] = A[high]
            high -= 1
        else:
            temp[i] = A[low]
            low += 1
 
        flag = bool(1-flag)
 
    for i in range(N):
        A[i] = temp[i]
    return A
n=int(input())
while n>0:
    N=int(input())
    A=list(map(int,input().split()))
    res=rearrange(A, N)
    print(*res)
    n-=1
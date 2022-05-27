l=list(map(int,input().split()))
l.sort()
k=l[-1]
s=l[-2]
res=(k-1)*(s-1)
print(res)
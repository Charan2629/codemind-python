n,m=map(int,input().split())
c=0
for i in range(n):
    l=list(map(int,input().split()))
    r=sorted(l)
    if sorted(l)==l or r[::-1]==l:
        c+=1
print(c)
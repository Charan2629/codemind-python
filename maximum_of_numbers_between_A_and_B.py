n=int(input())
l=list(map(int,input().split()))
k,m=map(int,input().split())
l.sort()
a=[]
flag=0
for i in l:
    if i>=k and i<=m:
        a.append(i)
        flag=1
if flag:
    print(max(a))
else:
    print(-1)
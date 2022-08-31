n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
k=[]
flag=0
for i in l:
    if i<a or i>b:
        k.append(i)
        flag=1
if flag:
    print(*k)
else:
    print(-1)
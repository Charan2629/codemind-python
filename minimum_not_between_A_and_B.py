n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
a=[]
flag=0
for i in l:
    if i<s or i>e:
        a.append(i)
        flag=1
if flag==0:
    print(-1)
else:
    print(min(a))
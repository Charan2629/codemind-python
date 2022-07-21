n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
Sum=0
flag=0
a=[]
b=[]
for x in range(s,e+1):
    a.append(x)
for i in l:
    if i not in a:
        b.append(i)
        flag=1
if flag==1:
    print(*b)
else:
    print(-1)
n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
flag=0
a=[]
b=[]
for i in range(s,e+1):
    a.append(i)
for x in l:
    if x not in a:
        b.append(x)
        flag=1
if flag:
    print(max(b))
else:
    print(-1)
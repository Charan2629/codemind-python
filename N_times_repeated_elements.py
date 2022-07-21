n=int(input())
l=list(map(int,input().split()))
k=int(input())
l1=[]
flag=0
for i in l:
   if l.count(i)==k and i not in l1:
       l1.append(i)
       flag=1
if flag:
    print(*l1)
else:
    print(-1)
n=int(input())
l=list(map(int,input().split()))
b=[]
flag=0
c=0
for i in l:
    if i not in b:
        if l.count(i)==i:
            b.append(i)
            c+=1
            flag=1
if flag:
    print(min(b),max(b))
else:
    print(-1)
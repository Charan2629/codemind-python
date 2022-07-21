n=int(input())
l=list(map(int,input().split()))
b=[]
flag=0
for i in l:
    if i not in b:
        if l.count(i)==i:
            b.append(i)
            flag=1
if flag:
    print(*b)
else:
    print(-1)
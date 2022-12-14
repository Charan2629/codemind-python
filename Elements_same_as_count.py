n=int(input())
l=list(map(int,input().split()))
flag=1
r=[]
for i in l:
    if i not in r:
        r.append(i)
for i in r:
    if l.count(i)==i:
        print(i,end=' ')
        flag=0
if flag:
    print(-1)
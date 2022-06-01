n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
s=[]
flag=0
for i in k:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c==1:
        s.append(i)
        flag=1
if flag:
    for i in s:
        print(i,end=(' '))
else:
    print('-1')
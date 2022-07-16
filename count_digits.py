n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i<0:
        i=(-1*i)
        a.append(int(len(str(i))))
    else:
        a.append(int(len(str(i))))
print(*a)
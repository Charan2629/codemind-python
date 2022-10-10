n,m=map(int,input().split())
a=[]
b=[]
c=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in a:
    for j in i:
        if j%2==0:
            b.append(j)
        else:
            c.append(j)
print(sum(b),sum(c))
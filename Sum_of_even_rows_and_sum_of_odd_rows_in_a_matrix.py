n,m=map(int,input().split())
a=[]
b=[]
c=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(0,n,2):
    b.append(sum(a[i]))
for i in range(1,n,2):
    c.append(sum(a[i]))
print(sum(b),sum(c))
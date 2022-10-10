n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in a:
    for j in i:
        b.append(j)
print(sum(b))
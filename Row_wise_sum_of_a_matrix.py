n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for i in a:
    Sum=0
    for j in i:
        Sum+=j
    b.append(Sum)
print(*b)
n,m=map(int,input().split())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    for i in l:
        a.append(sum(l))
print(max(a))
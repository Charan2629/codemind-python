p,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
k=0
s=0
c=set(a)
d=list(set(b))
for i in d:
    if i not in c:
        s+=1
for i in c:
    if i not in d:
        k+=1
print(s+k)
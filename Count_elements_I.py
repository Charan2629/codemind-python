s,s1=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=set(b)
d=list(set(a))
s=0
for i in d:
    if i in c:
        s+=1
print(s)
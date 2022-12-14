n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n//2):
    a.append(l[i])
for i in range(n//2,n):
    b.append(l[i])
print(sum(a))
print(sum(b))
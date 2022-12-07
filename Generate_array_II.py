n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    if i%2==1:
        a.append(l[i])
h=0
for i in range(len(a)):
    k=a[i]
    for j in range(k):
        print(l[h],end=' ')
    h+=2
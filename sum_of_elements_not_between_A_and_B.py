n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
Sum=0
for i in range(len(l)):
    if l[i]<s or l[i]>e:
        Sum+=l[i]
print(Sum)
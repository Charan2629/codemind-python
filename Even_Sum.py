n=int(input())
l=list(map(int,input().split()))
Sum=0
for i in range(n):
    if l[i]%2==0:
        Sum+=l[i]
print(Sum)
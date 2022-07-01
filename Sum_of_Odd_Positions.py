n=int(input())
l=list(map(int,input().split()))
Sum=0
for i in range(n):
    if i%2==1:
        Sum+=l[i]
print(Sum)
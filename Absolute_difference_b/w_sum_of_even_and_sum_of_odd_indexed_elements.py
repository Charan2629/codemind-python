n=int(input())
l=list(map(int,input().split()))
Sum,Sum1=0,0
for i in range(n):
    if i%2==0:
        Sum+=l[i]
    if i%2==1:
        Sum1+=l[i]
res=abs(Sum-Sum1)
print(res)
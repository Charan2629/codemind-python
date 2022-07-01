n=int(input())
l=list(map(int,input().split()))
Sum,Sum1=0,0
for i in l:
    if i%2==0:
        Sum+=i
    if i%2==1:
        Sum1+=i
res=abs(Sum-Sum1)
print(res)
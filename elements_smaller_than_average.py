n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in l:
    c+=i
avg=c//n
for i in l:
    if i<=avg:
        s+=1
print(s)
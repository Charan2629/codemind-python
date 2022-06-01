n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    c=0
    while(i>0):
        i//=10
        c+=1
    if c%2==0:
        s+=1
print(s)
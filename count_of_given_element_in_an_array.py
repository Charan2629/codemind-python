n=int(input())
l=list(map(int,input().split()))
s=int(input())
c=0
for i in l:
    if i==s:
        c+=1
print(c)
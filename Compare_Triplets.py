l=list(map(int,input().split()))
n=list(map(int,input().split()))
c,s=0,0
for i in range(0,3):
    if l[i]>n[i]:
        c+=1
    elif l[i]<n[i]:
        s+=1
print(c,s)
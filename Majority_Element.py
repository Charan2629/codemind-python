n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
for i in k:
    c=0
    for  j in l:
        if i==j:
            c+=1
    if c>n//2:
        print(i)
        break
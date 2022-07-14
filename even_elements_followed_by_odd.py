n=int(input())
l=list(map(int,input().split()))
nl=[]
for i in l:
    if i%2==0:
        nl.append(i)
for i in l:
    if i%2==1:
        nl.append(i)
for i in nl:
    print(i,end=' ')
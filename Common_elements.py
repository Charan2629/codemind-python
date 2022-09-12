a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
n=[]
ml=[]
for i in l1:
    if i in l2:
        n.append(i)
for i in n:
    if i not in ml:
        ml.append(i)
print(*ml)
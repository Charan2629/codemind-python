n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i<0:
        i=-1*i
    sq=i**2
    k.append(sq)
k.sort()
for i in k:
    print(i,end=' ')
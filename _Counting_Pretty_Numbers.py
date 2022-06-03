n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    count=0
    res=['2','3','9']
    for j in range(a,b+1):
        k=str(j)
        if k[len(k)-1] in res:
            count+=1
    print(count)
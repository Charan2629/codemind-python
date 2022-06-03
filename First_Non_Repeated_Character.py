n=int(input())
c,flag=0,0
for i in range(n):
    l=int(input())
    s=input()
    for i in s:
        c=s.count(i)
        if c==1:
            print(i)
            flag=1
            break
    else:
        print(-1)
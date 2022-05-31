n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    num=str(i)
    if("".join(reversed(num))==num):
        c+=1
print(c)
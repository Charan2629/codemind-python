s=input().split()
res=min(s[-1])
flag=0
for i in s[-1]:
    if ord(res)+32==ord(i):
        print(i)
        flag=1
if flag==0:
    print(min(s[-1]))
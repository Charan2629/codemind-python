n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
flag=0
Sum,c=0,0
for i in l:
    if i not in b:
        if l.count(i)==i:
            Sum+=i
            b.append(i)
            c+=1
            flag=1
if flag:
    print("%.2f" %(Sum/c))
else:
    print(-1)
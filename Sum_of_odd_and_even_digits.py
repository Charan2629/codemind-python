n=int(input())
o=0
e=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2==0:
        e=e+l[i]
    else:
        o+=l[i]
if (e-o)==0:
    print("YES")
else:
    print("NO")
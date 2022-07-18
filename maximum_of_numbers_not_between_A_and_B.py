n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
ll=[]
for i in l:
    if i<s or i>e:
        ll.append(i)
if len(ll)==0:
    print(-1)
else:
    print(max(ll)) 
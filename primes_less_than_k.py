def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
l=list(map(int,input().split()))
l.sort()
k=int(input())
c=0
for i in l:
    if i>1:
        if isprime(i):
            if i<=k:
                c+=1
print(c)
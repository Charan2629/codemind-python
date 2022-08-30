n=int(input())
a,b=0,1
print(0,end=' ')
for i in range(n-1):
    res=a+b
    print(res,end=' ')
    res,b,a=b,a,res
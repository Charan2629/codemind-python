n=int(input())
b=1
a=0
c=a+b
if n==1 :
    print(a)
else :
    print(a,end=" ")
    print(b,end=" ")
    for i in range(2,n) :
        c=a+b
        a=b
        b=c
        print(c,end=" ")
def lcm(a,b) :
    if a>b:
        a,b=b,a
    c=b
    while True :
        if c%a==0 and c%b==0 :
            return c
            break
        c+=1
a,b=map(int,input().split())
print(lcm(a,b))
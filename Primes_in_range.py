def is_prime(n):
    for i in range(2,int(n**0.5)+1) :
        if n%i==0 :
            return 0
    else:
        return 1
s=int(input())
e=int(input())
c=0
if s>1:
    for i in range(s,e+1) :
        if(is_prime(i)):
            c+=1
else :
    for i in range(s+1,e+1) :
        if(is_prime(i)):
            c+=1
print(c)
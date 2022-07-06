def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    else:
        return 1
s=int(input())
e=int(input())
if s==1:
    s=2
for i in range(s,e+1):
    if is_prime(i):
        print(i)
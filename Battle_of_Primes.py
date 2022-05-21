def is_prime(n):
    for i in range(2,int(n**0.5)+1) :
        if n%i==0 :
            return 0
    else:
        return 1
s=int(input())
e=int(input())
Sum=0
Summ=s+e
for i in range (1,50):
    Sum=Summ+i
    if(is_prime(Sum)):
        print(i)
        break
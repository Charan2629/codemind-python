n=int(input())
r=0
rev=0
rev2=0
sq=n*n

while n > 0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
    
sq2=rev*rev

while sq2 :
    r=sq2%10
    rev2=rev2*10+r
    sq2//=10

if sq==rev2 :
    print(True)
else :
    print(False)
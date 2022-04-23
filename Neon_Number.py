n=int(input())
Sum=0
sqr=n*n
while sqr>0 :
    r=sqr%10
    Sum+=r
    sqr=sqr//10

if Sum == n :
    print("Neon Number")
else :
    print("Not Neon Number")
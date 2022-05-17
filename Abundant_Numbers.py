n=int(input())
Sum=0
temp=n
for i in range (1,n//2+1) :
    if n%i==0 :
        Sum=Sum+i
if Sum > temp :
    print(True)
else :
    print(False)
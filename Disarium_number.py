n=int(input())
length=len(str(n))
c=0
Sum=0
temp=n
while(n):
    rem=n%10
    Sum=Sum+int(rem**length)
    n=n//10
    length-=1
if Sum==temp :
    print(True)
else :
    print(False)
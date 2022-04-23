n=int(input())
Sum=0
prod=1
while n > 0 :
    r=n%10
    Sum+=r
    prod*=r
    n=n//10

if Sum==prod :
    print("Spy Number")
else :
    print("Not Spy Number")
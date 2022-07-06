s=int(input())
Sum=0
prod=1
while s>0:
    rem=s%10
    Sum+=rem
    prod*=rem
    s//=10
if Sum==prod:
    print('Spy Number')
else:
    print('Not Spy Number')
n=int(input())
temp=n
Sum=0
s=n*n
while s>0:
    rem=s%10
    Sum+=rem
    s//=10
if Sum==temp:
    print('Neon Number')
else:
    print('Not Neon Number')
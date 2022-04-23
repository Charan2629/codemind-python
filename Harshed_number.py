n = int(input())
Sum = 0
temp = n
while n > 0 :
    r = n % 10
    Sum += r
    n = n // 10
if temp % Sum == 0 :
    print("True")
else :
    print("False")
n=int(input())
s=n*n
st=str(n)
sq=int(st[::-1])**2
ns=str(sq)
if str(s)[::-1]==ns:
    print(True)
else:
    print(False)
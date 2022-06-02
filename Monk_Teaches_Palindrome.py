n=int(input())
for i in range(n):
    s=input()
    flag=0
    if s==s[::-1]:
        flag=1
    if flag and len(s)%2==0:
        print('YES EVEN')
    elif flag and len(s)!=0:
        print('YES ODD')
    else:
        print('NO')
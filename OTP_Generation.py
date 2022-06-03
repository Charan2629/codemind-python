s=input()
n=[]
for i in s:
    if int(i)%2!=0:
        res=int(i)*int(i)
        n.append(res)
print(''.join(str(i) for i in n))
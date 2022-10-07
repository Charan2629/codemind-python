ns=input()
s=ns.lower()
a=[]
for i in s:
    if i not in a:
        a.append(i)
for i in a:
    if s.count(i)==1:
        print(i)
        break
else:
    print(-1)
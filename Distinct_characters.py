ns=input()
s=ns.lower()
a=[]
for i in s:
    if i not in a and i not in " ":
        a.append(i)
for i in sorted(a):
    if s.count(i)==1:
        print(i,end='')
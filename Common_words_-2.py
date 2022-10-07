s1=input().lower().split()
s2=input().lower().split()
a=[]
c=0
for i in s1:
    if i in s2:
        a.append(i)
for i in a:
    if s1.count(i)==1 and s2.count(i)==1:
        c+=1
print(c)
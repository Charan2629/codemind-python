s1=input().lower().split()
s2=input().lower().split()
a=[]
for i in s1:
    if i in s2:
        a.append(i)
print(len(a))
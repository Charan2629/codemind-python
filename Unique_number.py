n=int(input())
a=[]
for i in str(n):
    if i not in a:
        a.append(i)
if len(a)==len(str(n)):
    print("Unique Number")
else:
    print("Not Unique Number")
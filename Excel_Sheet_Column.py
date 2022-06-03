n=int(input())
str=""
res=0
while n:
    res=(n-1)%26
    str=chr(65+res)+str
    n=(n-1)//26
print(str)
n=int(input())
test_list = list(map(int,input().split()))
Sum=0
k = list(set(test_list))
for i in k:
    if i%2!=0:
        Sum+=i
print (Sum)
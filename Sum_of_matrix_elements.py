mtrxrows = int(input())
mtrxcols = int(input())
mtrx = []
for n in range(mtrxrows):
    l = list(map(int, input().split()))

    mtrx.append(l)
    
rslt_sum = 0
for n in range(mtrxrows):
    for m in range(mtrxcols):
        rslt_sum += mtrx[n][m]
print(rslt_sum)
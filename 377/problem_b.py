n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

totalAddedWalks = 0;
for i in range(len(a) - 1):
    if((a[i] + a[i+1]) < k):
        ExtraWalksReq = k - (a[i]+a[i+1])
        totalAddedWalks = totalAddedWalks + ExtraWalksReq 
        a[i+1] = a[i+1] + ExtraWalksReq
print(totalAddedWalks)
for ans in a:
    print(ans, end=' ')
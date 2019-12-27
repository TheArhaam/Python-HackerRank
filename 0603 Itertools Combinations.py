import itertools

a = input().split()
arr = list(sorted(a[0]))
k = int(a[1])
res = []
for i in range(1,k+1):
    res = res + list(itertools.combinations(arr,i))

for item in res:
    print(''.join(item))



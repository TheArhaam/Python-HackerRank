import itertools

a = input().split()
arr = list(sorted(a[0]))
k = int(a[1])

res = list(itertools.permutations(arr,k))

for item in res:
    print(''.join(item))

import itertools
a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = list(itertools.product(a,b))

res = " ".join([str(elem) for elem in res])

print(res)
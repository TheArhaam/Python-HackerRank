n = int(input())
a = set(list(map(int,input().split())))
m = int(input())
b = set(list(map(int,input().split())))

res = a.union(b)

print(len(res))
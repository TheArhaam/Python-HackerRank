n = int(input())
a = set(list(map(int,input().split())))
m = int(input())
b = set(list(map(int,input().split())))

res = a.symmetric_difference(b)

print(len(res))


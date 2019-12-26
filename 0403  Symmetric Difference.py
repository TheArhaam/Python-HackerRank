n1 = int(input())
m = set(list(map(int,input().split())))
n2 = int(input())
n = set(list(map(int,input().split())))

#Values in m and not n
res = m.difference(n)
#Adding values present in n and not m
res.update(n.difference(m))
#Sorting the set
res = sorted(res)

#Displaying set
for item in res:
    print(item)
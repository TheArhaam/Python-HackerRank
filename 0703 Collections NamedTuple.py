import collections
n = int(input())
cols = input().split()
data = collections.namedtuple('data',[item for item in cols])
studlist = []
for i in range(n):
    info = input().split()
    temp = data(*info)
    studlist.append(temp)

total = 0
for item in studlist:
    total = total + int(item.MARKS)

avg = total/n

print(avg)


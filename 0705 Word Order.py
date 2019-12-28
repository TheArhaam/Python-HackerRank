from collections import Counter

n = int(input())
arr = [input() for i in range(n)]

c = Counter(arr)

print(len(c))

count = [c[i] for i in c]
count = ' '.join(list(map(str,count)))
print(count)
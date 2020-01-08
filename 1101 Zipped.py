a = list(map(int,input().split()))
n = a[0]
x = a[1]

subs = []

for i in range(x):
    temp = list(map(float,input().split()))
    subs.append(temp)
# One of the following is the reason zip(*subs) works and zip(subs) doesn't
# Using * to capture items during tuple unpacking
# Using * to unpack iterables into a list/tuple
tempzip = zip(*subs)

for i in tempzip:
    print(sum(i)/len(i))
 
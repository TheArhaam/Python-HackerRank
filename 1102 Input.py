a = list(map(int,input().split()))
x = a[0]
k = a[1]

poly = input().split()

for i in range(len(poly)):
    if(poly[i] == 'x'):
        poly[i] = str(x)

res = eval(''.join(poly))

if(res == k):
    print('True')
else:
    print('False')
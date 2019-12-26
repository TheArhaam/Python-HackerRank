setlen = int(input())
a = set(list(map(int,input().split())))
n = int(input())

for i in range(0,n):
    command = input().split()
    nset = set(list(map(int,input().split())))
    c = 'a.' + command[0] + '(nset)'
    eval(c)

res = 0
for item in a:
    res = res + item

print(res)

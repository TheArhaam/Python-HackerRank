n = int(input())
s = set(map(int, input().split()))

num = int(input())

for i in range(0,num):
    command = input().split()
    if(command[0] == 'pop'):
        s.pop()
    else:
        c = "s." + command[0] + "(" + command[1] + ")"
        eval(c)

res = 0
for item in s:
    res = res + item

print(res)
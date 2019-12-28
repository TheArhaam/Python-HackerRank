from collections import deque

n = int(input())
d = deque()
for i in range(n):
    command = input().split()
    if(len(command)==1):
        eval('d.'+command[0]+'()');
    else:
        eval('d.'+command[0]+'('+command[1]+')')

res = ' '.join(list(map(str,d)))
print(res)
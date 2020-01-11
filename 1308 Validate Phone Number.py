
import re

n = int(input())

for i in range(n):
    number = input()
    regex = '^[789]{1}[0-9]{9}$'
    res = re.match(regex,number)
    if(res):
        print('YES')
    else:
        print('NO')
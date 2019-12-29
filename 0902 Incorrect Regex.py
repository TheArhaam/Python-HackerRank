import re

n = int(input())

for i in range(n):
    res = True
    try:
        pattern = re.compile(input())
    except re.error as e:
        res = False
    print(res)


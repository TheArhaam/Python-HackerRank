import re

n = int(input())

for i in range(n):
    regex = '^[+,-]{0,1}[0-9]*[.]{1}[0-9]+$'
    temp = input()
    tempres = re.match(regex,temp)
    if(tempres):
        print('True')
    else:
        print('False')
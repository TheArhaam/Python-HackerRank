import re

n = int(input())

for i in range(n):
    string = input()
    str1 = re.sub('((?<=\s)&&(?=\s))','and',string)
    str2 = re.sub('((?<=\s)\|\|(?=\s))','or',str1)
    print(str2)
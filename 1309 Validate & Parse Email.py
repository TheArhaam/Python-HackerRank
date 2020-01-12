import re
import email.utils

n = int(input())

for i in range(n):
    string = input()
    str1 = email.utils.parseaddr(string)[1]
    regex = '^[a-zA-Z]{1}[a-zA-Z0-9._-]+[@]{1}[a-zA-Z]+[.]{1}[a-zA-Z]{1,3}$'
    res = re.match(regex,str1)
    if(res):
        print(string)
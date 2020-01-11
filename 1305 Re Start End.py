import re

s = input()
k = input()

# regex = "(?=["+k+"])"

# res = re.finditer(regex,k)

# if(res):
#     for item in res:
#         print("("+str(item.start())+","+str(item.end())+")")
# else:
#     print("(-1,-1)")

res = list(re.finditer(r'(?={})'.format(k), s))
if res:
    print('\n'.join(str((item.start(),
          item.start() + len(k) - 1)) for item in res))
else:
    print('(-1, -1)')
import re

string = input()
vowels = 'aeiouAEIOU'
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
regex = '(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])'

# for i in range(0,len(string)):
#     for j in range(i,len(string)-i):
#         temp = string[i:j]
#         tempre = re.match(regex,temp)
#         if(tempre):
#             print(temp)

tempre = re.findall(regex,string)
if(tempre):
    print('\n'.join(tempre))    
else:
    print('-1')

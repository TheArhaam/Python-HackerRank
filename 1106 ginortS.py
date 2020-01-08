
string = list(input())

lower = []
upper = []
oddNum = []
evenNum = []
for i in string:
    # lower
    if(i.isalpha() and i.islower()):
        lower.append(i)
    # upper
    elif(i.isalpha() and i.isupper()):
        upper.append(i)
    # oddNum
    elif(i.isdigit() and (int(i)%2!=0)):
        oddNum.append(i)
    # evenNum
    elif(i.isdigit() and (int(i)%2==0)):
        evenNum.append(i)    
res = sorted(lower) + sorted(upper) + sorted(oddNum) + sorted(evenNum)

print(''.join(res))

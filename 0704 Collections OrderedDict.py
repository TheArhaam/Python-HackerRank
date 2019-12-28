from collections import OrderedDict 
n = int(input())

od = OrderedDict()

for i in range(n):
    temp = input().split()
    name = ''
    price = 0
    for j in range(len(temp)):
        if(temp[j].isalpha()):
            name = name + temp[j] + ' '
        elif(temp[j].isdigit()):
            price = price + int(temp[j])
    if(name in od):
        od[name] = od[name] + price
    else:
        od[name] = price

for i in od:
    print(i + str(od[i]))

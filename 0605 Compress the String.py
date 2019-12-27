numlist = list(map(int,input()))
size = len(numlist)
i = 0
res = []

while(i<size):
    count = 1
    j = i + 1
    while(j<size and numlist[i] == numlist[j]):
        count = count + 1
        numlist.remove(numlist[j])
        size = size - 1
    temp = '('+str(count)+', '+str(numlist[i])+')'
    res.append(temp)
    i = i + 1

print(' '.join(res))


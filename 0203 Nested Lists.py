scorelist = []
mainlist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelist.append(score)
        mainlist.append([name,score])

#Removing duplicates
scorelist = list(dict.fromkeys(scorelist))

#Sorting
scorelist.sort()

#Finding the second lowest grade
res = scorelist[1]

reslist = []
for [name,score] in mainlist:
    if(score == res):
        reslist.append(name)

#Sorting reslist
reslist.sort()

#Printing reslist
for name in reslist:
    print(name)

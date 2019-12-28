from collections import deque

t = int(input())

for i in range(t):
    n = int(input())
    sides = deque(map(int,input().split()))
    
    # print(sides)
    while(len(sides)!=1 and sides[0]>=sides[1]):
        sides.popleft()
        # print(sides)
    while(len(sides)!=1 and sides[-1]>=sides[-2]):
        sides.pop()  
        # print(sides)

    if(len(sides) == 1):
        print('Yes')
    else:
        print('No')
    

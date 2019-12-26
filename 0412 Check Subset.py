t = int(input())

for i in range(0,t):
    na = int(input())
    a = set(list(map(int,input().split())))
    nb = int(input())
    b = set(list(map(int,input().split())))
    if(a.issubset(b)):
        print('True')
    else:
        print('False')

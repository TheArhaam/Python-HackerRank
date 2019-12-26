a = set(list(map(int,input().split())))
n = int(input())

superset = True

for i in range(0,n):
    b = set(list(map(int,input().split())))
    if(not b<a):
        superset = False
        break;

print(superset)

n,m = input().split()
n = int(n)
m = int(m)
arr = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = set(a)
b = set(b)
happiness = 0

for item in arr:
    if(item in a):
        happiness = happiness + 1
    elif(item in b):
        happiness = happiness - 1

print(happiness)


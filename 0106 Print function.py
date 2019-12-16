if __name__ == '__main__':
    n = int(input())

res = 0
for i in range(1,n+1):
    if (i<10):
        res = (res*10)+i
    elif (i>=10 and i<100):
        res = (res*100)+i
    elif (i>=100 and i<1000):
        res = (res*1000)+i

print(res)

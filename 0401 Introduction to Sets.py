def average(array):
    dset = set(array)
    res = 0
    for i in dset:
        res = res + i
    res = res/len(dset)
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
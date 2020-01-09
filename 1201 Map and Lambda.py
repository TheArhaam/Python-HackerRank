cube = lambda x: x*x*x

def fibonacci(n):
    res = []
    first = 0
    second = 1
    if(n<=0):
        return res
    elif(n == 1):
        res.append(first)
    elif(n == 2):
        res.append(first)
        res.append(second)
    else:
        res.append(first)
        res.append(second)
        n = n-2
        third = int()
        for i in range(n):
            third = first + second
            res.append(third)
            first = second
            second = third

    return res


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
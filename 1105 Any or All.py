# VERSION-1
# def checkSign(a):
#     if (a>=0):
#         return True
#     elif (a<0):
#         return False

# def checkPalindrome(a):
#     if (str(a) == str(a)[::-1]):
#         return True
#     else:
#         return False

# def checkNum(a):
#     return any([checkSign(a),checkPalindrome(a)])

# res = []

n = int(input())

a = list(map(int,input().split()))

# for i in a:
#     res.append(checkNum(i))

# print(any(res))

# VERSION 2

print(all([i>0 for i in a]) and any([str(j) == str(j)[::-1] for j in a]))
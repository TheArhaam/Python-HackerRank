n = int(input())

for i in range(n):
    num = input().split()
    try:
        print(int(num[0])//int(num[1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
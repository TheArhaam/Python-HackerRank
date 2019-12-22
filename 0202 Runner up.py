if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

arrlist = []

#Putting values into a list
for num in arr:
    arrlist.append(int(num))

#Removing duplicates from list
arrlist = list(dict.fromkeys(arrlist))

#Sorting list
arrlist.sort()

#Displaying 2nd last element (Runner-up)
print(arrlist[-2])

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

#Converting to Tuple
tn = tuple(integer_list)

#Generating Hash
htn = hash(tn)

#Printing Hash
print(htn)
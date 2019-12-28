import collections

x = int(input())                            #number of shoes
sizelist = list(map(int,input().split()))   #shoe sizes
n = int(input())                            #number of customers

shoecounter = collections.Counter(sizelist)             #counter for sizelist

earned = 0                                  

for i in range(0,n):
    a = input().split()
    size = int(a[0])
    price = int(a[1])
    if(shoecounter[size]):                  #Checking if shoe is available
        earned = earned + price
        shoecounter[size] = shoecounter[size] - 1

print(earned)
        


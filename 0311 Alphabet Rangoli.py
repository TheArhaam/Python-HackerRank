def print_rangoli(size):
    #Generating string of characters that will be used in rangoli
    alpha = 'abcdefghijklmnopqrstuvwxyz'[0:size]

    #Traversing from (size-1) to (-size) ex: e to a
    for i in range(size-1,-size,-1):
        #To get the proper index of alphabets
        x = abs(i) 
        #Generating the line to be printed
        line = alpha[size:x:-1] + alpha[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
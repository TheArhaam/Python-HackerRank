if __name__ == '__main__':
    N = int(input())

newlist = []
for i in range(0,N):
    command = input()
    command = command.split()
    if(command[0] == 'insert'):
        newlist.insert(int(command[1]),int(command[2]))
    elif (command[0] == 'print'):
        print(newlist)
    elif (command[0] == 'remove'):
        newlist.remove(int(command[1]))
    elif (command[0] == 'append'):
        newlist.append(int(command[1]))
    elif (command[0] == 'sort'):
        newlist.sort()
    elif (command[0] == 'pop'):
        newlist.pop()
    elif (command[0] == 'reverse'):
        newlist.reverse()

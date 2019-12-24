def merge_the_tools(string, k):
    rows = int(len(string)/k)

    t = []
    i=0
    while(i<len(string)):
        t.append(list(string[i:i+k]))
        i = i + k
    # print(t)
    
    u=[]
    for item in t:
        u.append(list(dict.fromkeys(item)))
    # print(u)
    
    for i in range(0,len(u)):
        u[i] = "".join(u[i])
    # print(u)

    u = "\n".join(u)
    print(u)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
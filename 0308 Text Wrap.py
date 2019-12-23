import textwrap

def wrap(string, max_width):
    res = ""
    for i in range(0,len(string)):
        if((i%max_width==0) and i!=0):
            res = res + "\n"
        res = res + string[i]

    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
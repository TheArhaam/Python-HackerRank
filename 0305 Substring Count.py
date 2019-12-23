def count_substring(string, sub_string):
    count = 0
    loop = (len(string) - len(sub_string))+1
    for i in range(0,loop):
        k=i
        j=0
        while((j<len(sub_string)) and (k<len(string)) and (string[k] == sub_string[j])):
            k = k + 1
            j = j + 1
        if(j==len(sub_string)):
            count = count + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
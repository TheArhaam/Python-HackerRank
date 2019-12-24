def minion_game(string):
    stuartpts = 0
    kevinpts = 0

    vowels = 'AEIOU'

    for i in range(len(s)):
        if s[i] in vowels:
            kevinpts += (len(string)-i)
        else:
            stuartpts += (len(string)-i)

    if(kevinpts > stuartpts):
        print('Kevin', kevinpts)
    elif(stuartpts > kevinpts):
        print('Stuart', stuartpts)
    else:
        print('Draw')
            
            

if __name__ == '__main__':
    s = input()
    minion_game(s)
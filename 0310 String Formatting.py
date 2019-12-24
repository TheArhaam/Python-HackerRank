def print_formatted(number):
    width = number.bit_length()
    res=""
    for i in range(1,number+1):
        res = res +\
        str(i).rjust(width)+" "+\
        str(oct(i).replace('0o','')).rjust(width)+" "+\
        str(hex(i).replace('0x','')).rjust(width).upper()+" "+\
        str(bin(i).replace('0b','')).rjust(width)+" "
        if(i!=number):
            res = res + '\n'

    print(res)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
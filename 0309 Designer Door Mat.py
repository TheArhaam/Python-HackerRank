r, c = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(c, '-') for i in range(r//2)]
print('\n'.join(pattern + ['WELCOME'.center(c, '-')] + pattern[::-1]))

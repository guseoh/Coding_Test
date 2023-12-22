# 알파벳 찾기

# s = [0] * 26
a = list(input())
s = 'abcdefghijklmnopqrstuvwxyz'

for i in s:
    if i in a:
        print(a.index(i), end=' ')
    else:
        print(-1, end=' ')
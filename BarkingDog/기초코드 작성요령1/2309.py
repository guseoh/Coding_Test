# 일곱 난쟁이
from sys import stdin
s = []

for _ in range(9):
    a = int(stdin.readline())
    s.append(a)

s.sort()

for i in range(9):
    if ((sum(s) - s[i]) - 100) in s:
        s.remove(s[i])
    elif (sum(s) - s[i]) == 100:
        s.remove(s[i])
        break

for i in range(7):
    print(s[i])
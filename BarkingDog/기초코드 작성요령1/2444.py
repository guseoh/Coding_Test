# 별 찍기-7

a = int(input())

for i in range(1, a+1):
    print(' ' * (a - i) + '*' * (2 * i - 1))

for i in range(a,1,-1):
    print(' ' * (a-i + 1) + '*' * (2 * i -3))
    
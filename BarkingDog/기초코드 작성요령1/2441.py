# 별 찍기 -4

a = int(input())

for i in range(a,0,-1):
    print(' ' * (a-i) + '*' * i)
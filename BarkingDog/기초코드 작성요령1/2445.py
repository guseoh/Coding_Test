# 별 찍기-8

a = int(input())

for i in range(1, a+1):
    print('*' * (i) + ' ' * (2*a - 2*i) + '*' * (i))
for i in range(1,a):
    print('*' * (a-i) + ' ' * (2 * i) + '*' * (a-i))
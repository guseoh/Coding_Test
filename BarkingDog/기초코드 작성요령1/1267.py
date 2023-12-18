# 핸드폰 요금
Y = []
M = []

a = int(input())
s = list(map(int, input().split()))

for i in range(a):
    x = 0
    y = 0
    
    x = s[i] // 30
    y = s[i] // 60
    
    if s[i] > 0:
        Y.append(x * 10 + 10)
        M.append(y * 15 + 15)
    else:
        Y.append(x * 10)
        M.append(y * 15)

if sum(Y) > sum(M):
    print('M', sum(M))
elif sum(Y) < sum(M):
    print('Y', sum(Y))
else:
    print('Y', 'M', sum(Y))

N = int(input())
li = list(map(int, input().split()))
y = m = 0
for n in li:
    y += (n//30 + 1) * 10
    m += (n//60 + 1) * 15
if m == y:
    print("Y M", m)
elif m < y:
    print("M", m)
else:
    print("Y", y)
# AttributeError: 'map' object has no attribute 'split'
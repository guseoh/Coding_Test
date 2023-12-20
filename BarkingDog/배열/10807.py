# 개수 세기

a = int(input())
n = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(a):
    if n[i] == v:
        cnt += 1
print(cnt)
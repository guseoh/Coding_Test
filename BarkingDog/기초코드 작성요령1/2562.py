# 최댓값

s = []

for _ in range(9):
    a = int(input())
    s.append(a)
print(max(s))
print(s.index(max(s)) + 1)
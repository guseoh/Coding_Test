s = []

for _ in range(5):
    a = int(input())
    s.append(a)
s.sort()
print(sum(s) // 5)
print(s[2])
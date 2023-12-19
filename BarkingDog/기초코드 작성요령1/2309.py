# 일곱 난쟁이
# from sys import stdin
# s = []

# for _ in range(9):
#     a = int(stdin.readline())
#     s.append(a)

# s.sort()

# for i in range(9):
#     if ((sum(s) - s[i]) - 100) in s:
#         s.remove(s[i])
#     elif (sum(s) - s[i]) == 100:
#         s.remove(s[i])
#         break

# for i in range(7):
#     print(s[i])

one = 0
two = 0
s = []

for _ in range(9):
    a = int(input())
    s.append(a)

for i in range(8):
    for j in range(i+1, 9):
        if sum(s) - (s[i]+ s[j]) == 100:
            one = s[i]
            two = s[j]
s.remove(one)
s.remove(two)
s.sort()
for i in s:
    print(i)
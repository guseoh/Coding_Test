# 숫자의 개수

# s = [0] * 10

# a = int(input())
# b = int(input())
# c = int(input())

# x = a * b * c

# for i in str(x):
#     s[int(i)] += 1

# for x in s:
#     print(x)

a = int(input())
b = int(input())
c = int(input())

s = list(str(a*b*c))
print(s)

# for i in range(10):
#     print(s.count(str(i)))
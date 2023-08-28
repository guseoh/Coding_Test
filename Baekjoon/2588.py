a = int(input())
b = int(input())

c = b % 10
d = b - c  # 385 - 5 = 380 


print(a * (c))
print(a * ((d // 10) % 10))
print(a * (d // 100))
print(a * b)
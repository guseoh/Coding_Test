# 카드 역배치
x = [x for x in range(1,21)] # x = [*range(1,21)]

for _ in range(10):
    a,b = map(int, input().split())
    x[a-1:b] =  x[a-1:b:][::-1]
    
print(*x)

# n = [int(i) for i in range(1,21)]
# for _ in range(10):
#     a,b = map(int, input().split())
#     n = n[:a-1] + n[a-1:b:][::-1] + n[b:]
# print(" ".join(map(str, n)))
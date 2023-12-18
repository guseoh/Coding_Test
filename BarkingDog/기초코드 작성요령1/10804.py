# 카드 역배치
x = [x for x in range(1,21)]

for _ in range(10):
    a,b = map(int, input().split())
    x[:a] + x[a:b+1:-1] + x[b:]
    print(x)

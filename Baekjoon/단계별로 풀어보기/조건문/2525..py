a,b = map(int, input().split())
c = int(input())

# 30 + 20 50
# 40 + 80 120
# 48 + 25 76

if (b + c > 60):
    z = b + c
    if (a == 23):
        print((z // 60) - 1, 60 - (z % 60))
    else:
        print(a + (z // 60), 60 - (z % 60))
else:
    print(a, b + c)
a,b = map(int, input().split())

if (b >= 45):
    print(a, b - 45)
else:
    if (a == 0):
        print(23, 60 - (45 - b))
    else:
        print(a - 1,  60 - (45 - b))

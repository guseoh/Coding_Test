a = []
for _ in range(7):
    x = int(input())
    if x % 2 == 1: 
        a.append(x)
if len(a) >= 1:
    print(sum(a))
    print(min(a))
else: print(-1)
a = []
for _ in range(10):
    c = 0
    x = int(input())
    
    c = x % 42
    if c not in a:
        a.append(c)
print(len(a))
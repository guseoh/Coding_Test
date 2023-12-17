a,b = map(int, input().split())
z = list(map(int, input().split())) # a
s= []
for i in range(a):
    if z[i] < b:
        s.append(z[i])

print(*s)


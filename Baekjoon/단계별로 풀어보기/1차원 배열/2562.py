max = 0
z = 0
a = []
for i in range(9):
    a.append(int(input()))
    if a[i] > max:
        max = a[i]
        z = i
print(max)
print(z+1)

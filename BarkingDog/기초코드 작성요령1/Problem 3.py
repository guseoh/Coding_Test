def func3(n):
    for i in range(1, n):
        if(i * i == n): return 1
    return 0
print(func3(8))
n,m = map(int, input().split())

a = [c for c in range(1, n+1)]

for _ in range(m):
    i,j = map(int, input().split())
    
    a = a[:n-1] + a[n-1:m][::-1] + a[m:]
    
print(' '.join(map(str. a)))
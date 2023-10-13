n,m = map(int, input().split()) # n: 바구니 개수, M: 공을 바꾸는 횟수
# a = []

# for i in range(1,n+1):
#     a.append(i)

a = [c for c in range(1,n+1)]

for _ in range(m):
    x = 0
    i,j = map(int, input().split())
    
    x = a[i-1]
    a[i-1] = a[j-1]
    a[j-1] = x
    
print(' '.join(map(str,a)))



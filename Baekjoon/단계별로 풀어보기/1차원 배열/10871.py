a, b = map(int, input().split())
aa = list(map(int, input().split()))

for i in range(a):
    if(aa[i] < b):
        print(aa[i], end=' ')


# IndexError: list index out of range: 리스트를 순회할 때 존재하지 않는 항목에 접근하려고 한다.

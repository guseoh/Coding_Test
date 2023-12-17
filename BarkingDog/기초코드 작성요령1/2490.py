for i in range(3):
    a = list(map(int, input().split()))
    x = a.count(0)
    if x == 1: print('A') # µµ
    elif x == 2: print('B')
    elif x == 3: print('C')
    elif x == 4: print('D')
    else: print('E')

# 두 수의 합

a = int(input())
s = list(map(int, input().split()))    
s.sort()
score = int(input())

cnt = 0
left = 0
right = len(s) - 1

while(left < right):
    
    if s[left] + s[right] == score:
        cnt += 1
        left += 1
        right -= 1
    elif s[left] + s[right] < score:
        left += 1
    else: right -= 1
    
print(cnt) 



# left, right 사용
# 목표값보다 작으면 left +=1
# 목표값보다 크면 right -= 1
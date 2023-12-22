# 방 번호

s = [x for x in range(10)]
z = []
a = list(input())

for i in range(9):
    x = 0
    if i == 6:
        x = (a.count(str(s[i]))) // 2
    else:
        x = a.count(str(s[i]))

    if x >=1:
        z.append(x)
        
print(max(z))

# 9966시 문제 발생

room = input()

count = [0] * 10

for i in room:
    count[int(i)] += 1

count[6] = (count[6] + count[9] +1 ) // 2
count[9] = 0

print(max(count))
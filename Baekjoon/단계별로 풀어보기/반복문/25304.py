a = int(input())
sum = 0

for i in range(int(input())):
    aa, bb = map(int, input().split())
    sum += (aa * bb)

if(sum == a):
    print("Yes")
else: print("No")
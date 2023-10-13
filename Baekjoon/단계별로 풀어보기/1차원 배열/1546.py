m = int(input())

# a = list(map(int, input().split()))
a = [x for x in map(int, input().split())] 
aa = max(a)

sum = sum(a)
print(sum * 100 / aa / m)
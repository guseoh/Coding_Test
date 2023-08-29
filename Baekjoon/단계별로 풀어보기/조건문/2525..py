a,b = map(int, input().split())
c = int(input())
# z = b + c

# if (z >= 60):
#     if (a == 23):
#         print((z // 60) - 1, (z % 60)) 
#     else:
#         print(a + (z // 60), (z % 60))
# else:
#     print(a, z)


z = b + c
hour = (z) // 60
min  = (z) % 60

if z >= 60:
    if(a + hour >= 24):
        a -= 24
    a += hour
    print(a, min)

else:
    if(a >= 24):
        a -= 24
    print(a, z)


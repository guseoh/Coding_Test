# Strfty
# 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만들어내는 함수


# for _ in range(int(input())):
#     a,b = map(str, input().split())
#     cnt = 0
#     for i in range(len(a)):
#         if a[i] not in b:
#             cnt += 1
#             break
#     if cnt >= 1:
#         print("Impossible")

#     else:
#         print("Possible")

def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

for _ in range(int(input())):
    a = input().split()
    if anagrams(a[0], a[1]):
        print("Possible")
    else: print("Impossible")
    
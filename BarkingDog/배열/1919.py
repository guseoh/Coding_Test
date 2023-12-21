# 에너그램 만들기
# 두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을때, 그러한 두 단어의 관계

a = list(input())
b = list(input())

alph = [0] * 26

for i in a:
    alph[ord(i) - 97] += 1
for i in b:
    alph[ord(i) - 97] -= 1

cnt = 0
for s in alph:
    cnt += abs(s)
print(cnt)
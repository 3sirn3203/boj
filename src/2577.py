a = int(input())
b = int(input())
c = int(input())
res = a * b * c
ans = [0] * 10
while res:
    ans[res % 10] += 1
    res = res // 10
for a in ans:
    print(a)
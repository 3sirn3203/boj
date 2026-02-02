import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
dp_a = [[0] * n for _ in range(n)]
dp_b = [[0] * m for _ in range(m)]
sub_a, sub_b = [], []

for i in range(n):
    for j in range(i, n):
        if i == j:
            dp_a[i][j] = a[i]
        else:
            dp_a[i][j] = dp_a[i][j - 1] + a[j]
        sub_a.append(dp_a[i][j])

for i in range(m):
    for j in range(i, m):
        if i == j:
            dp_b[i][j] = b[i]
        else:
            dp_b[i][j] = dp_b[i][j - 1] + b[j]
        sub_b.append(dp_b[i][j])

sub_a = sorted(sub_a)
sub_b = sorted(sub_b)
cnt_a = [1] * len(sub_a)
cnt_b = [1] * len(sub_b)

prev, flag, start_idx = sub_a[0], False, 0
for i in range(1, len(sub_a)):
    if prev == sub_a[i]:
        if not flag:
            start_idx = i - 1
            flag = True
        if i == len(sub_a) - 1:
            for j in range(start_idx, len(sub_a)):
                cnt_a[j] = i - start_idx + 1
    else:
        if not flag:
            prev = sub_a[i]
        else:
            for j in range(start_idx, i):
                cnt_a[j] = i - start_idx
            prev = sub_a[i]
            flag = False

prev, flag, start_idx = sub_b[0], False, 0
for i in range(1, len(sub_b)):
    if prev == sub_b[i]:
        if not flag:
            start_idx = i - 1
            flag = True
        if i == len(sub_b) - 1:
            for j in range(start_idx, len(sub_b)):
                cnt_b[j] = i - start_idx + 1
    else:
        if not flag:
            prev = sub_b[i]
        else:
            for j in range(start_idx, i):
                cnt_b[j] = i - start_idx
            prev = sub_b[i]
            flag = False

ans = 0
for element in sub_b:
    tmp = -1
    left, right = 0, len(sub_a) - 1
    while left <= right:
        mid = (left + right) // 2
        if element + sub_a[mid] == t:
            tmp = mid
            break
        elif sub_a[mid] < t - element:
            left = mid + 1
        else:
            right = mid - 1
    if tmp >= 0:
        ans += cnt_a[tmp]

print(ans)
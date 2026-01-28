import sys

input = sys.stdin.readline

n = int(input())
trees = list(map(int, input().split()))
falls = list(map(int, input().split()))
ds = [(trees[i] + falls[i] - 1) // falls[i] for i in range(n)]

left, right = 0, max(ds)
ans = right
def check(val):
    if not val:
        return False
    cum = 0
    for d in ds:
        if d > 2 * val:
            return False
        if d > val:
            cum += (d - val)
            if cum > val:
                return False
    return cum <= mid

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
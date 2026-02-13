import sys

input = sys.stdin.readline
T = int(input())

def is_valid(n, m):
    q, r = divmod(n, 3)
    cum = (3 * 3 * q * (q + 1) // 2)
    if r == 1:
        cum += 3 * q + 1
    elif r == 2:
        cum += 3 * (q + 1) + 3 * q + 1
    else:
        cum -= 2
    if cum <= m:
        return True
    else:
        return False

for _ in range(T):
    m = int(input())
    ans = 0
    lo, hi = 0, m
    while lo <= hi:
        mid = (lo + hi) // 2
        if is_valid(mid, m):
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1
    print(ans + 1)

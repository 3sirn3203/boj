import sys

input = sys.stdin.readline
T = int(input())

def first_step_to_zero(N: int) -> int:
    def dec(t: int) -> int:
        m, r = divmod(t, 3)
        return (3 * m * (m + 1)) // 2 + r * (m + 1)

    lo, hi = 0, 1
    while dec(hi) <= N:
        hi *= 2

    while lo < hi:
        mid = (lo + hi) // 2
        if dec(mid) > N:
            hi = mid
        else:
            lo = mid + 1
    return lo - 1

for _ in range(T):
    m = int(input())
    ans = 1
    tmp = (m + 2) // 3
    ans += first_step_to_zero(tmp)
    print(ans)
    
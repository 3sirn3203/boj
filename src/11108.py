import sys

input = sys.stdin.readline
MAX_TIME = 10081

def solve(tvs, N):
    dp = [0] * MAX_TIME
    tvs_sorted = sorted(tvs, key=lambda x: x[0])

    best = 0
    idx = 0

    for tv in tvs_sorted:
        s, d, p = tv
        while idx <= s:
            best = best if dp[idx] < best else dp[idx]
            idx += 1
        dp[s + d] = max(dp[s + d], best + p)

    while idx < MAX_TIME:
        best = best if dp[idx] < best else dp[idx]
        idx += 1
    return best


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        tvs = [tuple(map(int, input().split())) for _ in range(N)]
        print(solve(tvs, N))

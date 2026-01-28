import sys

input = sys.stdin.readline

n, k = map(int, input().split())
w, v = [], []
for _ in range(n):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0] * (k + 1) for _ in range(n)]
for i in range(n):
    for j in range(1, k + 1):
        if w[i] <= j:
            if not i:
                dp[i][j] = v[i]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            if not i:
                dp[i][j] = dp[i - 1][j]
            
print(dp[n - 1][k])
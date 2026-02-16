import sys

input = sys.stdin.readline

MOD = 1000000007
n, k = map(int, input().split())
nums = input()
dp = [[[0, 0] for _ in range(k)] for _ in range(n)]
if nums[0] == "0":
    dp[0][0][0] = 1
else:
    dp[0][0][1] = 1

for i in range(1, n):
    for j in range(k):
        if j == 0:
            dp[i][j][1] = dp[i - 1][j][1]
        else:
            if nums[i] == "0":
                dp[i][j][1] = dp[i - 1][j][1]
                dp[i][j][0] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]) % MOD
            else:
                dp[i][j][1] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j][1]) % MOD

print(sum(dp[n - 1][k - 1]) % MOD)
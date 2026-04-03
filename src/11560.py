import sys

input = sys.stdin.readline


def solve(k, n):
    dp = [[0] * (k * (k + 1)) for _ in range(k)]
    dp[0][0], dp[0][1] = 1, 1

    for i in range(1, k):
        for j in range((i + 1) * (i + 2) // 2 + 1):
            for idx, d in enumerate(dp[i - 1]):
                if not d:
                    continue
                if idx <= j and idx + i + 1 >= j:
                    dp[i][j] += d

    return dp[k - 1][n]
    

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        k, n = map(int, input().split())
        print(solve(k, n))
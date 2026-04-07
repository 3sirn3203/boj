import sys

input = sys.stdin.readline


def solve(N):
    dp = [0] * (N + 1)
    prev = [0] * (N + 1)

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1
        if not i % 2 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2
        if not i % 3 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3
    
    path = []
    target = N
    while True:
        path.append(target)
        if target == 1:
            break
        target = prev[target]

    return dp[N], path


if __name__ == "__main__":
    N = int(input())
    ans, path = solve(N)
    print(ans)
    print(*path)

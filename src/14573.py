import sys

input = sys.stdin.readline
MOD = 1_000_000_007

def solve(query, dp_res, dp_res_sum):
    if query[0] == 1:
        target = min(query[2], query[3])
        print(dp_res[target] * query[1] % MOD)
    elif query[0] == 2:
        target = max(query[2], query[3])
        f, cnt = query[1], 0
        while f % 2 == 0:
            cnt += 1
            f //= 2
        if target > 2:
            print((cnt + target - 1) % MOD)
        else:
            print(cnt % MOD)
    elif query[0] == 3:
        print((dp_res_sum[query[3]] * query[1] % MOD - dp_res_sum[query[2] - 1] * query[1] % MOD) % MOD)
        # print(((dp_res_sum[query[3]] - dp_res_sum[query[2] - 1]) % MOD) * query[1] % MOD)
    else:
        print(dp_res[query[2]] * query[1] % MOD)


if __name__ == "__main__":
    q = int(input())
    dp, dp_sum, dp_res, dp_res_sum = [0] * 1_000_001, [1] * 1_000_001, [1] * 1_000_001, [0] * 1_000_001
    dp[0], dp_res_sum[1] = 1, 1
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] * 2 % MOD
    for i in range(3, len(dp_sum)):
        dp_sum[i] = ((dp[i - 3] + 1) % MOD) * dp_sum[i - 1] % MOD
    for i in range(3, len(dp_res)):
        dp_res[i] = dp_sum[i] * dp[i - 2] % MOD
    for i in range(2, len(dp_res_sum)):
        dp_res_sum[i] = (dp_res[i] + dp_res_sum[i - 1]) % MOD

    for _ in range(q):
        query = list(map(int, input().split()))
        solve(query, dp_res, dp_res_sum)
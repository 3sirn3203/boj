import sys

input = sys.stdin.readline

def solve(n, numbers):
    ans = 0
    
    def solve_dp(nums):
        dp = [1] * n
        for idx in range(n):
            for jdx in range(idx):
                if nums[idx] > nums[jdx]:
                    dp[idx] = max(dp[idx], dp[jdx] + 1)
        return dp

    dp_l2r = solve_dp(numbers)
    dp_r2l = solve_dp(numbers[::-1])[::-1]

    for x, y in zip(dp_l2r, dp_r2l):
        tmp = x+ y
        ans = ans if ans > tmp else tmp
    return ans - 1

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    print(solve(n, numbers))

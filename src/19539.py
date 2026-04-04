import sys

input = sys.stdin.readline

def solve(N, heights):
    h_sum = sum(heights)
    if h_sum % 3 != 0:
        return "NO"
    else:
        t = h_sum // 3
        cap = sum(x // 2 for x in heights)
        return "YES" if cap >= t else "NO"

if __name__ == "__main__":
    N = int(input())
    heights = list(map(int, input().split()))
    print(solve(N, heights))
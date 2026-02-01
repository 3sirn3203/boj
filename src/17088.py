import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
ans = float('inf')

if n == 1 or n == 2:
    print(0)
    exit()

def search(idx, cum, diff):
    global ans
    if idx == n:
        ans = cum if cum < ans else ans
        return
    if cum >= ans:
        return
    if not idx:
        search(idx + 1, cum, diff)

        b[idx] += 1
        search(idx + 1, cum + 1, diff)
        b[idx] -= 1

        b[idx] -= 1
        search(idx + 1, cum + 1, diff)
        b[idx] += 1
        return
    if diff is None:
        search(idx + 1, cum, b[idx] - b[idx - 1])

        b[idx] += 1
        search(idx + 1, cum + 1, b[idx] - b[idx - 1])
        b[idx] -= 1

        b[idx] -= 1
        search(idx + 1, cum + 1, b[idx] - b[idx - 1])
        b[idx] += 1
        return
    else:
        if b[idx] - b[idx - 1] == diff:
            search(idx + 1, cum, diff)
        if b[idx] + 1 - b[idx - 1] == diff:
            b[idx] += 1
            search(idx + 1, cum + 1, diff)
            b[idx] -= 1
        if b[idx] - 1 - b[idx - 1] == diff:
            b[idx] -= 1
            search(idx + 1, cum + 1, diff)
            b[idx] += 1

search(0, 0, None)
print(ans if ans != float('inf') else -1)
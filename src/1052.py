import sys

input = sys.stdin.readline

def solve(n, k):
    bottles, idx = [0] * 30, 0
    bottles[0] = n
    while True:
        bottle = bottles[idx]
        q, r = divmod(bottle, 2)
        if q:
            bottles[idx + 1], bottles[idx] = q, r
            idx += 1
        else:
            break
    ans, now = 0, sum(bottles)
    if now > k:
        cum, idx = 0, None
        for i in range(len(bottles) - 1, -1, -1):
            if bottles[i] == 1:
                cum += 1
            if cum == k:
                idx = i
                break
        cum = 0
        for i in range(idx):
            if bottles[i] == 1:
                cum += 2 ** i
        ans = 2 ** idx - cum
    print(ans)


if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k)

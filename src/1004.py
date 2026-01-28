t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    ans = 0
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    for _ in range(n):
        x, y, r = map(int, input().split())
        if (dist(x1, y1, x, y) < r) ^ (dist(x2, y2, x, y) < r):
            ans += 1
    print(ans)
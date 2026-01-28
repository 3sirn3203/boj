n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    sub = abs(r1 - r2)
    ans = None
    if dist == 0 and r1 == r2:
        ans = -1
    elif dist < r1 + r2 and dist > sub:
        ans = 2
    elif dist == r1 + r2 or dist == sub:
        ans = 1
    else:
        ans = 0
    print(ans)
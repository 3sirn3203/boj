import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
    
    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

n = int(input())
s = [tuple(map(int, input().split())) for _ in range(n)]
s.sort(key=lambda x: x[2])

coords = sorted(list(set(a for a, _, _ in s) | set(c for _, _, c in s)))
idx = {v: i + 1 for i, v in enumerate(coords)}

fw = BIT(len(coords))
a_set = set(a for a, _, _ in s)
ans = 0
for a in a_set:
    fw.add(idx[a], 1)
    ans += 1

for a, b, c in s:
    fw.add(idx[a], -1)

    l = bisect_left(coords, b) + 1
    r = bisect_right(coords, c)
    cnt = fw.range_sum(l, r)

    if not cnt:
        fw.add(idx[c], 1)
        ans += 1
    
    fw.add(idx[a], 1)

print(ans)
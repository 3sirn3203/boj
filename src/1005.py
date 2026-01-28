import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, r = map(int, input().split())
    tm = list(map(int, input().split()))
    ttl = [-1] * (n)
    g = defaultdict(list)
    for _ in range(r):
        s, e = map(int, input().split())
        g[e].append(s)
    trgt = int(input())

    def f(nw):
        if not g[nw]:
            return tm[nw - 1]
        if ttl[nw - 1] > -1:
            return ttl[nw - 1]
        tmp = []
        for bfr in g[nw]:
            tmp.append(f(bfr) + tm[nw - 1])
        ttl[nw - 1] = max(tmp)
        return ttl[nw - 1]
    
    print(f(trgt))
import sys

sys.setrecursionlimit(10**6)
inpt = sys.stdin.readline

INF = 10 ** 8
n, q = map(int, inpt().split())
tree = [-1] * 4 * n
tm = [-1] * n

def init(l, r, idx):
    if l == r:
        tree[idx] = l
        return tree[idx]
    mid = (l + r) // 2
    lr = init(l, mid, idx * 2)
    rr = init(mid + 1, r, idx * 2 + 1)
    tree[idx] = lr if lr < rr else rr
    return tree[idx]

def query(lt, rt, l, r, idx):
    if r < lt or rt < l:
        return INF
    if lt <= l and r <= rt:
        return tree[idx]
    mid = (l + r) // 2
    lq = query(lt, rt, l, mid, idx * 2)
    rq = query(lt, rt, mid + 1, r, idx * 2 + 1)
    return lq if lq < rq else rq

def update(l, r, t, idx, diff):
    if t < l or r < t:
        return tree[idx]
    if l == r:
        tree[idx] = diff
        return tree[idx]
    mid = (l + r) // 2
    lu = update(l, mid, t, idx * 2, diff)
    ru = update(mid + 1, r, t, idx * 2 + 1, diff)
    tree[idx] = lu if lu < ru else ru
    return tree[idx]

init(0, n - 1, 1)
for cnt in range(1, q + 1):
    t, idx = map(int, inpt().split())
    if t == 1:
        res = query(idx - 1, n - 1, 0, n - 1, 1)
        if res < INF:
            print(res + 1)
            tm[res] = cnt
            update(0, n - 1, res, 1, INF)
        else:
            print(-1)
    else:
        if tm[idx - 1] > 0:
            print(tm[idx - 1])
            tm[idx - 1] = -1
            update(0, n - 1, idx - 1, 1, idx - 1)
        else:
            print(-1)

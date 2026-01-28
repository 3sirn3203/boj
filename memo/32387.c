#include <stdio.h>
#define INF 100000000

int n, q;
int tree[4000000];
int tm[1000000];

int init(int l, int r, int idx) {
    if (l == r) {
        tree[idx] = l;
        return tree[idx];
    }
    int mid = (l + r) / 2;
    int lr, rr;
    lr = init(l, mid, idx * 2);
    rr = init(mid + 1, r, idx * 2 + 1);
    tree[idx] = lr < rr ? lr : rr;
    return tree[idx];
}

int query(int lt, int rt, int l, int r, int idx) {
    if (r < lt || rt < l) return INF;
    if (lt <= l && r <= rt) return tree[idx];
    int mid = (l + r) / 2;
    int lq, rq;
    lq = query(lt, rt, l, mid, idx * 2);
    rq = query(lt, rt, mid + 1, r, idx * 2 + 1);
    return lq < rq ? lq : rq;
}

int update(int l, int r, int t, int idx, int diff) {
    if (t < l || r < t) return tree[idx];
    if (l == r) {
        tree[idx] = diff;
        return tree[idx];
    }
    int mid = (l + r) / 2;
    int lu, ru;
    lu = update(l, mid, t, idx * 2, diff);
    ru = update(mid + 1, r, t, idx * 2 + 1, diff);
    tree[idx] = lu < ru ? lu : ru;
    return tree[idx];
}

int main() {
    scanf("%d %d", &n, &q);
    init(0, n - 1, 1);
    for(int cnt = 1; cnt <= q; ++cnt) {
        int t, idx;
        scanf("%d %d", &t, &idx);
        if (t == 1) {
            int res = query(idx - 1, n - 1, 0, n - 1, 1);
            if (res < INF) {
                printf("%d\n", res + 1);
                tm[res] = cnt;
                update(0, n - 1, res, 1, INF);
            }
            else printf("-1\n");
        }
        else {
            if (tm[idx - 1] > 0) {
                printf("%d\n", tm[idx - 1]);
                tm[idx - 1] = -1;
                update(0, n - 1, idx - 1, 1, idx - 1);
            }
            else printf("-1\n");
        }
    }
}
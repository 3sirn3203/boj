import sys
import copy

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
original = [list(map(int, input().split())) for _ in range(n)]

ans = -1
def mv_left(game):
    for i in range(n):
        modified = [False] * n
        for j in range(1, n):
            if not game[i][j]:
                continue
            k = j - 1
            res = 0
            while True:
                if k < 0:
                    res = 1
                    break
                if not game[i][k]:
                    k -= 1
                    continue
                elif game[i][k] == game[i][j] and not modified[k]:
                    res = 2
                    modified[k] = True
                    break
                else:
                    res = 3
                    break
            if res == 1:
                game[i][0], game[i][j] = game[i][j], 0
            elif res == 2:
                game[i][k] *= 2
                game[i][j] = 0
            elif res == 3 and k + 1 != j:
                game[i][k + 1], game[i][j] = game[i][j], 0
    return game
def mv_right(game):
    for i in range(n):
        modified = [False] * n
        for j in range(n - 2, -1, -1):
            if not game[i][j]:
                continue
            k = j + 1
            res = 0
            while True:
                if k >= n:
                    res = 1
                    break
                if not game[i][k]:
                    k += 1
                    continue
                elif game[i][k] == game[i][j] and not modified[k]:
                    res = 2
                    modified[k] = True
                    break
                else:
                    res = 3
                    break
            if res == 1:
                game[i][n - 1], game[i][j] = game[i][j], 0
            elif res == 2:
                game[i][k] *= 2
                game[i][j] = 0
            elif res == 3 and k - 1 != j:
                game[i][k - 1], game[i][j] = game[i][j], 0
    return game
def mv_top(game):
    for i in range(n):
        modified = [False] * n
        for j in range(1, n):
            if not game[j][i]:
                continue
            k = j - 1
            res = 0
            while True:
                if k < 0:
                    res = 1
                    break
                if not game[k][i]:
                    k -= 1
                    continue
                elif game[k][i] == game[j][i] and not modified[k]:
                    res = 2
                    modified[k] = True
                    break
                else:
                    res = 3
                    break
            if res == 1:
                game[0][i], game[j][i] = game[j][i], 0
            elif res == 2:
                game[k][i] *= 2
                game[j][i] = 0
            elif res == 3 and k + 1 != j:
                game[k + 1][i], game[j][i] = game[j][i], 0
    return game
def mv_bottom(game):
    for i in range(n):
        modified = [False] * n
        for j in range(n - 2, -1, -1):
            if not game[j][i]:
                continue
            k = j + 1
            res = 0
            while True:
                if k >= n:
                    res = 1
                    break
                if not game[k][i]:
                    k += 1
                    continue
                elif game[k][i] == game[j][i] and not modified[k]:
                    res = 2
                    modified[k] = True
                    break
                else:
                    res = 3
                    break
            if res == 1:
                game[n - 1][i], game[j][i] = game[j][i], 0
            elif res == 2:
                game[k][i] *= 2
                game[j][i] = 0
            elif res == 3 and k - 1 != j:
                game[k - 1][i], game[j][i] = game[j][i], 0
    return game
def search(cum, game):
    if cum == 5:
        global ans
        tmp = max(map(max, game))
        ans = ans if ans > tmp else tmp
        return
    lgame = mv_left(copy.deepcopy(game))
    search(cum + 1, lgame)
    rgame = mv_right(copy.deepcopy(game))
    search(cum + 1, rgame)
    tgame = mv_top(copy.deepcopy(game))
    search(cum + 1, tgame)
    bgame = mv_bottom(copy.deepcopy(game))
    search(cum + 1, bgame)

search(0, original)
print(ans)
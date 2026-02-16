import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(n, board):
    ans = 0

    def copy_board(b):
        return [row[:] for row in b]

    def move_line_left(line):
        modified = [False] * n
        for i in range(1, n):
            if not line[i]:
                continue
            k = i - 1
            while True:
                if k < 0:
                    line[0], line[i] = line[i], 0
                    break
                if line[k] == 0:
                    k -= 1
                    continue
                if line[k] == line[i] and not modified[k]:
                    line[k] *= 2
                    line[i] = 0
                    modified[k] = True
                    break
                if k + 1 != i:
                    line[k + 1], line[i] = line[i], 0
                break

    def move(org_b, dir_):
        b = copy_board(org_b)

        if dir_ == 0:
            for i in range(n):
                move_line_left(b[i])
        elif dir_ == 1:
            for i in range(n):
                row = b[i][::-1]
                move_line_left(row)
                b[i] = row[::-1]
        elif dir_ == 2:
            for c in range(n):
                col = [b[r][c] for r in range(n)]
                move_line_left(col)
                for r in range(n):
                    b[r][c] = col[r]
        elif dir_ == 3:
            for c in range(n):
                col = [b[r][c] for r in range(n)][::-1]
                move_line_left(col)
                col = col[::-1]
                for r in range(n):
                    b[r][c] = col[r]
        return b

    def dfs(depth, org_b):
        nonlocal ans
        ans = max(ans, max(map(max, org_b)))
        if depth == 5:
            return
        for d in range(4):
            dfs(depth + 1, move(org_b, d))
    
    dfs(0, board)
    print(ans)

if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    solve(n, board)

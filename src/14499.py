import sys

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0]
def roll(d, mv):
    T, B, N, S, E, W = d
    if mv == 1:
        return [W, E, N, S, T, B]
    if mv == 2:
        return [E, W, N, S, B, T]
    if mv == 3:
        return [S, N, T, B, E, W]
    if mv == 4:
        return [N, S, B, T, E, W]
def move(x, y, mv):
    if mv == 1:
        if y + 1 >= m:
            return None
        else:
            return (x, y + 1)
    elif mv == 2:
        if y - 1 < 0:
            return None
        else:
            return (x, y - 1)
    elif mv == 3:
        if x - 1 < 0:
            return None
        else:
            return (x - 1, y)
    else:
        if x + 1 >= n:
            return None
        else:
            return (x + 1, y)


world = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    world.append(tmp)

cmds = list(map(int, input().split()))

for cmd in cmds:
    mv = move(x, y, cmd)
    if mv is None:
        continue
    else:
        x, y = mv
        dice = roll(dice, cmd)
        if world[x][y] == 0:
            world[x][y] = dice[1]
        else:
            dice[1] = world[x][y]
            world[x][y] = 0
        print(dice[0])


import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    end = int(n ** 0.5) * 2
    cnt = 0
    for i in range(2, end + 1):
        if not i % 2:
            if ((n % i) == i // 2) and (n // i) - (i - 1) // 2 > 0:
                cnt += 1
        else:
            if (not n % i) and (n // i - (i - 1) // 2 > 0):
                cnt += 1
    print(cnt)
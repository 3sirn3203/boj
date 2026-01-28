t = int(input())
for _ in range(t):
    n = int(input())
    fibo = [[0] * 41 for _ in range(2)]
    fibo[0][0] = 1
    fibo[1][1] = 1

    for i in range(2, n + 1):
        fibo[0][i] = fibo[0][i - 1] + fibo[0][i - 2]
        fibo[1][i] = fibo[1][i - 1] + fibo[1][i - 2]
    
    print(f"{fibo[0][n]} {fibo[1][n]}")

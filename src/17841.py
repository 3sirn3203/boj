import sys

input = sys.stdin.readline
MOD = 1_000_000_007
TARGET = ["U", "N", "I", "S", "T"]

def solve(N, words):
    dp = [[0] * (len(TARGET) + 1) for _ in range(N)]

    def find_idx(char):
        for idx in range(len(TARGET)):
            if TARGET[idx] == char:
                return idx
        return -1
    
    dp[0][0] = 1
    cum_length = 0
    while cum_length < len(TARGET):
        if words[0][cum_length] != TARGET[cum_length]:
            break
        dp[0][cum_length + 1] += 1
        cum_length += 1

    for word_idx in range(1, N):
        for tar_idx in range(len(TARGET) + 1):
            dp[word_idx][tar_idx] += dp[word_idx - 1][tar_idx]
        idx = find_idx(words[word_idx][0])
        if idx < 0:
            continue
        cum_length = 0
        while idx < len(TARGET):
            if words[word_idx][cum_length] != TARGET[idx]:
                break
            cum_length += 1
            dp[word_idx][idx + 1] = (dp[word_idx][idx + 1] + dp[word_idx - 1][idx + 1 - cum_length]) % MOD
            idx += 1

    return dp[N - 1][len(TARGET)]


if __name__ == "__main__":
    N = int(input())
    words = [input() for _ in range(N)]
    print(solve(N, words))

n = int(input())
for _ in range(2):
    iter_num, words = input().split()
    iter_num = int(iter_num)
    for word in words:
        print(word * iter_num, end='')
    print()
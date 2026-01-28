n = int(input())
print(1 if (not n % 4 and n % 100) or not n  % 400 else 0)
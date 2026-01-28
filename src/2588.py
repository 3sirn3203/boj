a = int(input())
b = int(input())
total = a * b
while b:
    print(a * (b % 10))
    b = b // 10
print(total)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(int(a * b / gcd(a, b)))
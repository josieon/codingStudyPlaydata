n = int(input())
m = list(map(int, input().split()))
count = 0

if n == len(m):
    for i in range(n):
        for j in range(2, m[i] + 1):
            if m[i] == j:
                count += 1
            if m[i] % j == 0:
                break

print(count)            
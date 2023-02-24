n, k = list(map(int, input().split()))
score = list(map(int, input().split()))
x = sorted(score)

print(x[n-k])
    
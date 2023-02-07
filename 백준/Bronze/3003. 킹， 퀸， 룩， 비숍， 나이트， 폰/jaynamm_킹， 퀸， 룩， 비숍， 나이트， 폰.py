n = list(map(int, input().split()))
chs = [1, 1, 2, 2, 2, 8]

for i in range(len(n)):
    print(chs[i] - n[i], end=" ")
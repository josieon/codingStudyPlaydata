n = int(input())
pp = [list(map(str, input().split())) for _ in range(n)]

pp.sort(key = lambda x : int(x[0]))

for i in range(n):
    print(*pp[i])
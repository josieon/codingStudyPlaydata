n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

nums.sort(key = lambda x:(x[0], x[1]))

for i in range(n):
    print(*nums[i])
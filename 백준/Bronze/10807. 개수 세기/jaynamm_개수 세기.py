n = int(input())
nums = map(int, input().split())
v = int(input())

cnt = [num for num in nums if v == num]

print(len(cnt))
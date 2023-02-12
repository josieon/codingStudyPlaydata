n, x = map(int, input().split())
nums = list(map(str, input().split()))
[print(num) for num in nums if int(num) < x]
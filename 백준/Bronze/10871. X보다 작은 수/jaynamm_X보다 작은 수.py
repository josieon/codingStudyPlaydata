n, x = map(int, input().split())
nums = list(map(str, input().split()))

low = [num for num in nums if int(num) < x]
print(' '.join(low))
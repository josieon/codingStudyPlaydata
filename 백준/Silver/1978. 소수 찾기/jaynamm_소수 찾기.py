n = int(input())
nums = list(map(int, input().split()))
result = 0

for num in nums:
    i = 2
    cnt = 1
    
    while num > 1:
        if num % i == 0:
            num = num // i
            cnt += 1
        else:
            i += 1
    
    if cnt == 2:
        result += 1
        
print(result)
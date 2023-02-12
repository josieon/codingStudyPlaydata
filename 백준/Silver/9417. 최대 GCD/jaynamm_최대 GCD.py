def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    mx = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            if mx < gcd(nums[i], nums[j]): 
                mx = gcd(nums[i], nums[j])
    print(mx)
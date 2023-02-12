def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(int(input())):
    n = list(map(int, input().split()))
    sum = 0
    
    for i in range(1, n[0]+1):
        for j in range(i, n[0]+1):
            if i != j:
                sum += gcd(n[i], n[j])
    print(sum)
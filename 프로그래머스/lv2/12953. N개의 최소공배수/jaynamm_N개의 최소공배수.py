def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def solution(arr):
    lcm = int(arr[0] * arr[1] / gcd(arr[0], arr[1]))
    
    for i in range(2, len(arr)):
        lcm = int(arr[i] * lcm / gcd(arr[i], lcm))
    
    return lcm
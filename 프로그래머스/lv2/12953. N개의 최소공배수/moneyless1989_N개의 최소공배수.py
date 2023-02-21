def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(arr):
    answer = 0
    if len(arr) == 1: answer = arr[0]
    answer = arr[0] * arr[1] / gcd(arr[0], arr[1])
    for x in arr[2:]:
        answer = answer * x / gcd(answer, x)
    return answer
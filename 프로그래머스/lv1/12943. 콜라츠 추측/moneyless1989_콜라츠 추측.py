def solution(n):
    for answer in range(500):
        if n == 1: return answer
        n = n/2 if n%2 == 0 else n*3+1
    return -1
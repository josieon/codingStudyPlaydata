def solution(n):
    for answer in range(500):
        if n == 1:
            return answer
        if n%2 == 0:
            n /= 2
        else:
            n = n*3 + 1
    if n != 1:
        return -1
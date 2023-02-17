def solution(n):
    i = 0
    
    while n >= 1:
        i += 1
        n = (n // i)
    
    return i-1
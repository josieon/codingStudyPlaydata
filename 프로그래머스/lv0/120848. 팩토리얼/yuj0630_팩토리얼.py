def solution(n):
    for i in range(1, 12):
        cnt = 1
        for j in range(1, i+1):
            cnt *= j
            if n < cnt:
                return i-1
        
        
    
def solution(n):
    answer = 0
    spl_num = []
    
    while n != 0:
        spn = n % 3
        spl_num.append(spn)
        n = n // 3
    
    spl_num = spl_num[::-1]
    
    for i in range(len(spl_num)):
        answer += spl_num[i] * 3**i

    return answer
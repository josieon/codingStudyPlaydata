def solution(X, Y):
    answer = ''
    xc = [0] * 10
    yc = [0] * 10
    
    for i in X:
        xc[int(i)] += 1
    for i in Y:
        yc[int(i)] += 1
    
    for i in range(9,-1,-1):
        if i == 0:
            if xc[i] and yc[i] and not answer:
                return "0"
        answer += (str(i) * min(xc[i], yc[i]))
        
    if answer == "":
        return "-1"
    
    return answer
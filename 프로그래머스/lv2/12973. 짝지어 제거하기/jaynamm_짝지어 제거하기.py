def solution(s):
    answer = -1
    
    stk = []
    ap = list(s)
    
    for i in range(len(ap)):
        if len(stk) == 0:
            stk.append(ap[i])
        elif stk[-1] == ap[i]:
            stk.pop()
        else:
            stk.append(ap[i])
            
    if len(stk) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer
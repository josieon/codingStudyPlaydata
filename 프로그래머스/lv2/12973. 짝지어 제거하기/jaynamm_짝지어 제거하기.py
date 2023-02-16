def solution(s):
    answer = -1
    stack = []
    
    for c in s:
        if not(stack):
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    if not(stack):
        answer = 1
    else:
        answer = 0
        
    return answer
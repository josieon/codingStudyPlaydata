def solution(numbers):
    answer = ''
    
    snum = list(map(str, numbers))
    snum.sort(key = lambda x:x*3, reverse=True)
    answer = str(int("".join(snum)))
    
    return answer
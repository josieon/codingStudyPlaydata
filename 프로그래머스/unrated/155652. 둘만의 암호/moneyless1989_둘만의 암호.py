def solution(s, skip, index):
    answer = ''
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for x in skip:
        alphabets = alphabets.replace(x, "")
    for x in s:
        target = alphabets.find(x)+index
        while target >= len(alphabets):
            target -= len(alphabets)
        answer += alphabets[target]
    return answer
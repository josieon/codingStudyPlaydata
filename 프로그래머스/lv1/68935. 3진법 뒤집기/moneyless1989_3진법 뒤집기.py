def solution(n):
    # n을 3진법으로 바꾸기
    string = ""
    while int(n) > 0:
        n = int(n)
        string += str(n%3)
        n /= 3
    # 10진법으로 다시 바꾸기
    answer = 0
    for idx, x in enumerate(reversed(string)):
        answer += int(x)*3**idx
    return answer
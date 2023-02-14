def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    for x in babbling:
        for y in pron:
            x = x.replace(y, "_")
        if x.replace("_", "") == "": answer += 1
    return answer
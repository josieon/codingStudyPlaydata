def solution(sizes):
    for x in sizes:
        if x[0] < x[1]:
            x[0], x[1] = x[1], x[0]
    sizes_T = list(zip(*sizes))
    answer = max(sizes_T[0]) * max(sizes_T[1])
    return answer 
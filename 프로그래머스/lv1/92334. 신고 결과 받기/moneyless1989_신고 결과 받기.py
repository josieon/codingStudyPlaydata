def solution(id_list, report, k):
    # 중복 제거
    report = set(report)
    answer = []
    send_report = {x:0 for x in id_list}
    attacked = {x:[] for x in id_list}
    killed = []
    for x in report:
        # 신고자 피신고자 분리
        names = x.split(" ")
        # 피신고 카운트 증가
        send_report[names[1]] += 1
        # 신고자가 신고한 상대 저장
        attacked[names[0]].append(names[1])
    # 정지당한 유저 저장
    for x in send_report:
        if send_report[x] >= k:
            killed.append(x)
    # 킬스코어 집계
    for x in attacked:
        kill = 0
        for y in attacked[x]:
            if y in killed: kill += 1
        answer.append(kill)
    return answer